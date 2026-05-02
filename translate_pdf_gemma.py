import argparse
import os
import re
import sys
import time
from pathlib import Path
from typing import Any

from huggingface_hub import InferenceClient
from pypdf import PdfReader
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


def extract_text_by_page(pdf_path: Path) -> list[str]:
    reader = PdfReader(str(pdf_path))
    texts = []
    for page in reader.pages:
        txt = page.extract_text() or ""
        texts.append(txt.strip())
    return texts


def init_ocr_engine() -> Any:
    try:
        import pytesseract
    except ImportError as exc:
        raise ImportError(
            "OCR 套件未安裝。請先執行：pip install -r requirements.txt"
        ) from exc
    return pytesseract


def ocr_page_text(
    fitz_page: Any,
    ocr_engine: Any,
    ocr_dpi: int,
    ocr_lang: str,
    tesseract_cmd: str | None,
) -> str:
    try:
        import fitz  # PyMuPDF
        from PIL import Image
    except ImportError as exc:
        raise ImportError(
            "OCR 需要 PyMuPDF 與 Pillow。請先執行：pip install -r requirements.txt"
        ) from exc

    if tesseract_cmd:
        ocr_engine.pytesseract.tesseract_cmd = tesseract_cmd

    try:
        _ = ocr_engine.get_tesseract_version()
    except Exception as exc:
        raise RuntimeError(
            "找不到 tesseract.exe。請先安裝 Tesseract OCR，或用 --tesseract-cmd 指定路徑。"
        ) from exc

    zoom = max(ocr_dpi, 72) / 72
    pix = fitz_page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=False)
    image_mode = "RGB" if pix.n < 4 else "RGBA"
    image = Image.frombytes(image_mode, (pix.width, pix.height), pix.samples)

    text = ocr_engine.image_to_string(image, lang=ocr_lang)
    return (text or "").strip()


def alnum_ratio(text: str) -> float:
    if not text:
        return 0.0
    alnum_count = sum(ch.isalnum() for ch in text)
    return alnum_count / max(len(text), 1)


def is_chart_like_page(fitz_page: Any, source_text: str, chart_drawings_min: int) -> bool:
    image_count = len(fitz_page.get_images(full=True))
    drawings_count = len(fitz_page.get_drawings())
    text_len = len((source_text or "").strip())

    has_visual_density = image_count > 0 or drawings_count >= chart_drawings_min
    sparse_text = text_len < 900
    return has_visual_density and sparse_text


def build_messages(page_no: int, source_text: str, target_lang: str) -> list[dict]:
    system_prompt = (
        "你是專業技術譯者。請把使用者提供的內容翻譯成"
        f"{target_lang}。"
        "保留原始數學式、符號、代碼與項目結構。"
        "不要省略任何內容；若原文看似 OCR 雜訊，請盡量忠實呈現。"
        "只輸出翻譯結果，不要額外解釋。"
    )

    user_prompt = (
        f"以下是 PDF 第 {page_no} 頁原文，請完整翻譯：\n\n"
        f"{source_text}"
    )

    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]


def translate_page(
    client: InferenceClient,
    models: list[str],
    page_no: int,
    source_text: str,
    target_lang: str,
    max_new_tokens: int,
    retries_per_model: int = 2,
    retry_base_seconds: float = 2.0,
) -> str:
    last_err = None
    for idx, model in enumerate(models, start=1):
        for attempt in range(1, retries_per_model + 1):
            try:
                response = client.chat.completions.create(
                    model=model,
                    messages=build_messages(page_no, source_text, target_lang),
                    temperature=1.0,
                    top_p=0.95,
                    max_tokens=max_new_tokens,
                )
                return response.choices[0].message.content.strip()
            except Exception as exc:
                last_err = exc
                wait_seconds = min(retry_base_seconds * (2 ** (attempt - 1)), 20)
                print(f"[警告] 第 {page_no} 頁翻譯失敗（模型 {model}，第 {attempt} 次）：{exc}")
                if attempt < retries_per_model:
                    print(f"[資訊] {wait_seconds:.1f} 秒後重試...")
                    time.sleep(wait_seconds)

        if idx < len(models):
            print(f"[資訊] 第 {page_no} 頁切換備援模型：{models[idx]}")

    raise RuntimeError(f"第 {page_no} 頁翻譯最終失敗：{last_err}")


def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description="使用 Gemma 31B 逐頁翻譯 PDF")
    parser.add_argument("--pdf", required=True, help="輸入 PDF 路徑")
    parser.add_argument(
        "--model",
        default="google/gemma-4-26b-it",
        help="Hugging Face 主要模型 ID（預設：google/gemma-4-26b-it）",
    )
    parser.add_argument(
        "--fallback-models",
        default="google/gemma-4-31b-it",
        help="備援模型清單（逗號分隔，預設：google/gemma-4-31b-it）",
    )
    parser.add_argument(
        "--target-lang",
        default="繁體中文",
        help="目標語言（預設：繁體中文）",
    )
    parser.add_argument("--start-page", type=int, default=1, help="起始頁（1-based）")
    parser.add_argument("--end-page", type=int, default=None, help="結束頁（1-based，含）")
    parser.add_argument(
        "--max-new-tokens",
        type=int,
        default=2048,
        help="每頁最大生成 token（預設：2048）",
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
        default=2,
        help="每個模型每頁重試次數（預設：2）",
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
        "--extract-only",
        action="store_true",
        help="只抽取 PDF 文字，不呼叫模型（測試用）",
    )
    parser.add_argument(
        "--ocr-mode",
        choices=["off", "on-empty", "all"],
        default="on-empty",
        help="OCR 模式：off=關閉，on-empty=僅空頁 OCR，all=全部頁 OCR（預設：on-empty）",
    )
    parser.add_argument(
        "--ocr-dpi",
        type=int,
        default=220,
        help="OCR 渲染 DPI（預設：220）",
    )
    parser.add_argument(
        "--ocr-lang",
        default="eng",
        help="Tesseract 語言包（預設：eng，例如 chi_tra+eng）",
    )
    parser.add_argument(
        "--tesseract-cmd",
        default=None,
        help="tesseract.exe 完整路徑（若未加到 PATH 可用）",
    )
    parser.add_argument(
        "--auto-chart-dpi",
        action="store_true",
        help="偵測圖表/低文字頁時，自動改用較高 DPI 再 OCR 一次",
    )
    parser.add_argument(
        "--ocr-high-dpi",
        type=int,
        default=340,
        help="圖表頁二次 OCR 的高 DPI（預設：340）",
    )
    parser.add_argument(
        "--ocr-min-chars",
        type=int,
        default=120,
        help="OCR 文字低於此字元數視為低品質（預設：120）",
    )
    parser.add_argument(
        "--ocr-min-alnum-ratio",
        type=float,
        default=0.18,
        help="OCR 文字英數比例低於此值視為低品質（預設：0.18）",
    )
    parser.add_argument(
        "--chart-drawings-min",
        type=int,
        default=60,
        help="判斷圖表頁的最少向量圖形數（預設：60）",
    )

    args = parser.parse_args()

    pdf_path = Path(args.pdf).expanduser().resolve()
    if not pdf_path.exists():
        raise FileNotFoundError(f"找不到 PDF：{pdf_path}")

    pages_text = extract_text_by_page(pdf_path)
    total_pages = len(pages_text)
    print(f"[資訊] 載入 PDF：{pdf_path.name}，總頁數：{total_pages}")

    fitz_doc = None
    ocr_engine = None
    if args.ocr_mode != "off":
        try:
            import fitz  # PyMuPDF
        except ImportError as exc:
            raise ImportError(
                "OCR 需要 PyMuPDF。請先執行：pip install -r requirements.txt"
            ) from exc
        fitz_doc = fitz.open(str(pdf_path))
        ocr_engine = init_ocr_engine()

    output_dir = Path(args.output_dir).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    base_name = sanitize_filename(pdf_path.stem)
    merged_output = output_dir / f"{base_name}.translated.md"

    target_pages = page_range(total_pages, args.start_page, args.end_page)

    api_key = os.environ.get("HF_TOKEN") or os.environ.get("HUGGINGFACEHUB_API_TOKEN")
    if not args.extract_only and not api_key:
        raise EnvironmentError(
            "找不到 Hugging Face API Token。Gemma 4 31B 這支腳本需要 HF_TOKEN（不是 GEMINI_API_KEY）。"
        )

    client = InferenceClient(api_key=api_key) if not args.extract_only else None
    model_list = [args.model]
    for m in [x.strip() for x in args.fallback_models.split(",") if x.strip()]:
        if m not in model_list:
            model_list.append(m)

    merged_parts: list[str] = []

    for p in target_pages:
        src = pages_text[p - 1]
        used_ocr = False
        used_high_dpi = False
        page_obj = fitz_doc[p - 1] if fitz_doc is not None else None

        chart_like = False
        if page_obj is not None and args.auto_chart_dpi:
            chart_like = is_chart_like_page(
                fitz_page=page_obj,
                source_text=src,
                chart_drawings_min=args.chart_drawings_min,
            )

        should_ocr = (
            args.ocr_mode == "all"
            or (args.ocr_mode == "on-empty" and not src)
            or (args.auto_chart_dpi and chart_like)
        )
        if should_ocr:
            ocr_text = ocr_page_text(
                fitz_page=page_obj,
                ocr_engine=ocr_engine,
                ocr_dpi=args.ocr_dpi,
                ocr_lang=args.ocr_lang,
                tesseract_cmd=args.tesseract_cmd,
            )

            low_quality = (
                len(ocr_text) < args.ocr_min_chars
                or alnum_ratio(ocr_text) < args.ocr_min_alnum_ratio
            )

            if (
                args.auto_chart_dpi
                and chart_like
                and low_quality
                and args.ocr_high_dpi > args.ocr_dpi
            ):
                ocr_text_high = ocr_page_text(
                    fitz_page=page_obj,
                    ocr_engine=ocr_engine,
                    ocr_dpi=args.ocr_high_dpi,
                    ocr_lang=args.ocr_lang,
                    tesseract_cmd=args.tesseract_cmd,
                )
                if len(ocr_text_high) >= len(ocr_text):
                    ocr_text = ocr_text_high
                    used_high_dpi = True

            if ocr_text:
                if not src or len(ocr_text) >= int(len(src) * 1.1):
                    src = ocr_text
                    used_ocr = True

        if not src:
            translation = "[此頁無可擷取文字，可能是掃描影像頁。可改用 OCR 流程。]"
        elif args.extract_only:
            translation = src
        else:
            print(f"[資訊] 正在翻譯第 {p} 頁...")
            translation = translate_page(
                client=client,
                models=model_list,
                page_no=p,
                source_text=src,
                target_lang=args.target_lang,
                max_new_tokens=args.max_new_tokens,
                retries_per_model=max(args.retries_per_model, 1),
                retry_base_seconds=max(args.retry_base_seconds, 0.2),
            )
            time.sleep(max(args.delay, 0))

        if used_ocr:
            print(f"[資訊] 第 {p} 頁已使用 OCR")
        if used_high_dpi:
            print(f"[資訊] 第 {p} 頁觸發高 DPI OCR（{args.ocr_high_dpi}）")

        page_file = output_dir / f"{base_name}.page-{p:04d}.md"
        page_file.write_text(translation + "\n", encoding="utf-8")

        merged_parts.append(f"## 第 {p} 頁\n\n{translation}\n")
        print(f"[完成] 第 {p} 頁 -> {page_file.name}")

    merged_output.write_text("\n".join(merged_parts), encoding="utf-8")
    print(f"[完成] 合併輸出：{merged_output}")

    if fitz_doc is not None:
        fitz_doc.close()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"[錯誤] {e}")
        sys.exit(1)
