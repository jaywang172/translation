import argparse
import os
import re
import sys
import time
from pathlib import Path
from typing import Any

import fitz  # PyMuPDF
from dotenv import load_dotenv


def sanitize_filename(name: str) -> str:
    safe = re.sub(r"[^\w\-\.]+", "_", name, flags=re.UNICODE)
    return safe.strip("_") or "output"


def page_range(total_pages: int, start_page: int, end_page: int | None):
    start = max(1, start_page)
    end = total_pages if end_page is None else min(total_pages, end_page)
    if start > end:
        raise ValueError(f"無效頁碼範圍：start_page={start_page}, end_page={end_page}")
    return range(start, end + 1)


def render_page_png_bytes(fitz_page: Any, dpi: int) -> bytes:
    zoom = max(dpi, 72) / 72
    pix = fitz_page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=False)
    return pix.tobytes("png")


def is_chart_like_page(fitz_page: Any, chart_drawings_min: int) -> bool:
    image_count = len(fitz_page.get_images(full=True))
    drawings_count = len(fitz_page.get_drawings())
    text_len = len((fitz_page.get_text("text") or "").strip())

    has_visual_density = image_count > 0 or drawings_count >= chart_drawings_min
    sparse_text = text_len < 900
    return has_visual_density and sparse_text


def build_page_prompt(page_no: int, target_lang: str) -> str:
    return (
        f"請將這一張 PDF 第 {page_no} 頁完整翻譯成{target_lang}。"
        "保留章節結構、條列、公式、符號與表格語意。"
        "若有圖表標題與座標文字也請翻譯。"
        "只輸出翻譯結果，不要加註解。"
    )


def parse_retry_after_seconds(error_text: str) -> float | None:
    # e.g. "Please retry in 52.548657132s."
    m = re.search(r"Please retry in\s+([0-9]+(?:\.[0-9]+)?)s", error_text)
    if m:
        return float(m.group(1))

    # e.g. "'retryDelay': '45s'"
    m = re.search(r"retryDelay'?:\s*'([0-9]+)s'", error_text)
    if m:
        return float(m.group(1))

    return None


def is_quota_error(error_text: str) -> bool:
    t = error_text.upper()
    return "RESOURCE_EXHAUSTED" in t or "QUOTA" in t or "429" in t


def load_existing_translation(output_dir: Path, base_name: str, page_no: int) -> str | None:
    page_file = output_dir / f"{base_name}.page-{page_no:04d}.md"
    if not page_file.exists():
        return None
    return page_file.read_text(encoding="utf-8").strip()


def rebuild_merged_output(output_dir: Path, base_name: str, total_pages: int, merged_output: Path) -> None:
    merged_parts: list[str] = []
    for p in range(1, total_pages + 1):
        page_file = output_dir / f"{base_name}.page-{p:04d}.md"
        if not page_file.exists():
            continue
        content = page_file.read_text(encoding="utf-8").strip()
        merged_parts.append(f"## 第 {p} 頁\n\n{content}\n")

    merged_output.write_text("\n".join(merged_parts), encoding="utf-8")


def translate_page_with_gemini(
    client: Any,
    types_module: Any,
    models: list[str],
    page_no: int,
    image_bytes: bytes,
    target_lang: str,
    retries_per_model: int = 4,
    base_retry_seconds: float = 2.0,
) -> str:
    prompt = build_page_prompt(page_no, target_lang)
    last_err = None

    for model_idx, model in enumerate(models, start=1):
        for attempt in range(1, retries_per_model + 1):
            try:
                response = client.models.generate_content(
                    model=model,
                    contents=[
                        types_module.Part.from_bytes(data=image_bytes, mime_type="image/png"),
                        prompt,
                    ],
                )
                text = (getattr(response, "text", "") or "").strip()
                if text:
                    return text
                raise RuntimeError("模型回傳空內容")
            except Exception as exc:
                last_err = exc
                err_text = str(exc)
                retry_after = parse_retry_after_seconds(err_text)
                wait_seconds = retry_after if retry_after is not None else min(base_retry_seconds * (2 ** (attempt - 1)), 90)

                print(
                    f"[警告] 第 {page_no} 頁翻譯失敗（模型 {model}，第 {attempt} 次）：{exc}"
                )

                if attempt < retries_per_model:
                    print(f"[資訊] {wait_seconds:.1f} 秒後重試...")
                    time.sleep(max(wait_seconds, 0.0))

        if model_idx < len(models):
            print(f"[資訊] 第 {page_no} 頁切換備援模型：{models[model_idx]}")
            if is_quota_error(str(last_err)):
                # 若是配額問題，先小等候避免瞬間打爆下一個模型
                time.sleep(2.0)

    raise RuntimeError(f"第 {page_no} 頁翻譯最終失敗：{last_err}")


def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description="使用 Google Gemini 逐頁翻譯 PDF（影像直送）")
    parser.add_argument("--pdf", required=True, help="輸入 PDF 路徑")
    parser.add_argument(
        "--model",
        default="gemini-2.5-flash",
        help="Gemini 模型（預設：gemini-2.5-flash）",
    )
    parser.add_argument(
        "--fallback-models",
        default="gemini-2.0-flash,gemini-1.5-flash",
        help="備援模型清單（逗號分隔），遇到額度/忙碌可自動切換",
    )
    parser.add_argument(
        "--target-lang",
        default="繁體中文",
        help="目標語言（預設：繁體中文）",
    )
    parser.add_argument("--start-page", type=int, default=1, help="起始頁（1-based）")
    parser.add_argument("--end-page", type=int, default=None, help="結束頁（1-based，含）")
    parser.add_argument(
        "--vision-dpi",
        type=int,
        default=240,
        help="一般頁影像 DPI（預設：240）",
    )
    parser.add_argument(
        "--auto-chart-dpi",
        action="store_true",
        help="遇到圖表/低文字頁，自動提高 DPI",
    )
    parser.add_argument(
        "--vision-high-dpi",
        type=int,
        default=360,
        help="圖表頁高 DPI（預設：360）",
    )
    parser.add_argument(
        "--chart-drawings-min",
        type=int,
        default=60,
        help="判斷圖表頁的最少向量圖形數（預設：60）",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.2,
        help="每頁請求間隔秒數（預設：0.2）",
    )
    parser.add_argument(
        "--retries-per-model",
        type=int,
        default=4,
        help="每個模型單頁重試次數（預設：4）",
    )
    parser.add_argument(
        "--retry-base-seconds",
        type=float,
        default=2.0,
        help="重試基礎等待秒數（預設：2.0）",
    )
    parser.add_argument(
        "--output-dir",
        default="translations",
        help="輸出資料夾（預設：translations）",
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="續跑模式：若頁面輸出檔已存在則跳過",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="只做頁面渲染與流程測試，不呼叫 Gemini",
    )

    args = parser.parse_args()

    pdf_path = Path(args.pdf).expanduser().resolve()
    if not pdf_path.exists():
        raise FileNotFoundError(f"找不到 PDF：{pdf_path}")

    doc = fitz.open(str(pdf_path))
    total_pages = len(doc)
    target_pages = page_range(total_pages, args.start_page, args.end_page)
    print(f"[資訊] 載入 PDF：{pdf_path.name}，總頁數：{total_pages}")

    output_dir = Path(args.output_dir).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    base_name = sanitize_filename(pdf_path.stem)
    merged_output = output_dir / f"{base_name}.translated.md"

    client = None
    types_module = None
    if not args.dry_run:
        api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
        if not api_key:
            raise EnvironmentError("找不到 Gemini API Key。請先設定 GEMINI_API_KEY。")

        try:
            from google import genai
            from google.genai import types
        except ImportError as exc:
            raise ImportError("缺少 google-genai 套件，請先執行：pip install -r requirements.txt") from exc

        client = genai.Client(api_key=api_key)
        types_module = types

    model_list = [args.model]
    fallback_list = [m.strip() for m in args.fallback_models.split(",") if m.strip()]
    for m in fallback_list:
        if m not in model_list:
            model_list.append(m)

    for p in target_pages:
        if args.resume:
            existing = load_existing_translation(output_dir, base_name, p)
            if existing:
                print(f"[跳過] 第 {p} 頁已存在，略過")
                continue

        page = doc[p - 1]
        chart_like = False
        if args.auto_chart_dpi:
            chart_like = is_chart_like_page(page, chart_drawings_min=args.chart_drawings_min)

        dpi = args.vision_dpi
        if args.auto_chart_dpi and chart_like and args.vision_high_dpi > args.vision_dpi:
            dpi = args.vision_high_dpi

        image_bytes = render_page_png_bytes(page, dpi=dpi)

        if args.dry_run:
            translation = f"[dry-run] 第 {p} 頁，使用 DPI={dpi}，影像大小={len(image_bytes)} bytes"
        else:
            print(f"[資訊] 正在翻譯第 {p} 頁（DPI={dpi}）...")
            translation = translate_page_with_gemini(
                client=client,
                types_module=types_module,
                models=model_list,
                page_no=p,
                image_bytes=image_bytes,
                target_lang=args.target_lang,
                retries_per_model=max(args.retries_per_model, 1),
                base_retry_seconds=max(args.retry_base_seconds, 0.2),
            )
            time.sleep(max(args.delay, 0))

        if dpi != args.vision_dpi:
            print(f"[資訊] 第 {p} 頁觸發高 DPI（{dpi}）")

        page_file = output_dir / f"{base_name}.page-{p:04d}.md"
        page_file.write_text(translation + "\n", encoding="utf-8")
        print(f"[完成] 第 {p} 頁 -> {page_file.name}")

    rebuild_merged_output(
        output_dir=output_dir,
        base_name=base_name,
        total_pages=total_pages,
        merged_output=merged_output,
    )
    print(f"[完成] 合併輸出：{merged_output}")
    doc.close()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"[錯誤] {e}")
        sys.exit(1)
