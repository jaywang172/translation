import argparse
import base64
import os
import re
import time
from pathlib import Path

from dotenv import load_dotenv
from huggingface_hub import InferenceClient


TEXT_EXTENSIONS = {".txt", ".md"}
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".heic", ".heif"}


def sanitize_filename(name: str) -> str:
    safe = re.sub(r"[^\w\-.]+", "_", name, flags=re.UNICODE)
    return safe.strip("_") or "question"


def read_text_file(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore").strip()


def image_file_to_data_url(path: Path) -> str:
    ext = path.suffix.lower()
    mime_map = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
        ".heic": "image/heic",
        ".heif": "image/heif",
    }
    mime_type = mime_map.get(ext, "application/octet-stream")
    b64 = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime_type};base64,{b64}"


def build_prompt_for_text(question_text: str) -> str:
    return (
        "請解以下線性代數題目，並以繁體中文輸出。\n"
        "輸出格式必須只包含三個一級標題，順序固定：\n"
        "# 題目復述\n"
        "# 解題過程\n"
        "# 用到的觀念\n\n"
        "要求：\n"
        "1) 題目復述：忠實重述題目，不改變條件。\n"
        "2) 解題過程：逐步推導並給出最終答案。\n"
        "3) 用到的觀念：條列關鍵線性代數觀念並簡要解釋。\n\n"
        "[題目原文開始]\n"
        f"{question_text}\n"
        "[題目原文結束]"
    )


def build_prompt_for_image() -> str:
    return (
        "請先讀取圖片中的線性代數題目，再以繁體中文解題。\n"
        "輸出格式必須只包含三個一級標題，順序固定：\n"
        "# 題目復述\n"
        "# 解題過程\n"
        "# 用到的觀念\n\n"
        "要求：\n"
        "1) 題目復述：忠實重述題目，不改變條件。\n"
        "2) 解題過程：逐步推導並給出最終答案。\n"
        "3) 用到的觀念：條列關鍵線性代數觀念並簡要解釋。"
    )


def build_system_prompt() -> str:
    return (
        "你是線性代數助教，請完整解題並用繁體中文輸出。"
        "輸出必須是 Markdown，並且只能包含以下三個一級標題，順序不可改：\n"
        "# 題目復述\n"
        "# 解題過程\n"
        "# 用到的觀念\n"
        "在『題目復述』要忠實重述題意（可整理語句但不能改變條件）。"
        "在『解題過程』要有步驟、計算與最後答案。"
        "在『用到的觀念』要條列解釋每個關鍵數學概念。"
        "若題目資訊不足，請明確寫出缺少哪些資訊，再提供可行的解題方向。"
    )


def normalize_model_for_provider(model_name: str, provider: str) -> str:
    model = model_name.strip()

    if provider == "gemini" and model.startswith("google/"):
        return model.split("/", 1)[1]

    if provider == "hf" and "/" not in model and model.startswith("gemma-"):
        return f"google/{model}"

    return model


def create_provider(model_name: str, forced_provider: str):
    provider = forced_provider
    if provider == "auto":
        gemini_api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
        hf_token = os.environ.get("HF_TOKEN") or os.environ.get("HUGGINGFACEHUB_API_TOKEN")

        if gemini_api_key:
            provider = "gemini"
        elif hf_token:
            provider = "hf"
        else:
            raise EnvironmentError(
                "找不到可用金鑰。請設定 GEMINI_API_KEY（建議）或 HF_TOKEN。"
            )

    if provider == "hf":
        hf_token = os.environ.get("HF_TOKEN") or os.environ.get("HUGGINGFACEHUB_API_TOKEN")
        if not hf_token:
            raise EnvironmentError("使用 Gemma 模型需要 HF_TOKEN 或 HUGGINGFACEHUB_API_TOKEN")
        return provider, InferenceClient(api_key=hf_token), None

    gemini_api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not gemini_api_key:
        raise EnvironmentError("使用 Gemini 模型需要 GEMINI_API_KEY 或 GOOGLE_API_KEY")

    try:
        from google import genai
        from google.genai import types
    except ImportError as exc:
        raise ImportError("缺少 google-genai，請先執行 pip install -r requirements.txt") from exc

    return provider, genai.Client(api_key=gemini_api_key), types


def solve_text_question(provider: str, client, types_module, model_name: str, text: str) -> str:
    if provider == "hf":
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": build_system_prompt()},
                {"role": "user", "content": build_prompt_for_text(text)},
            ],
            temperature=0.2,
            top_p=0.9,
            max_tokens=2048,
        )
        return (response.choices[0].message.content or "").strip()

    response = client.models.generate_content(
        model=model_name,
        contents=build_prompt_for_text(text),
    )
    return (response.text or "").strip()


def solve_image_question(provider: str, client, types_module, model_name: str, file_path: Path) -> str:
    if provider == "hf":
        data_url = image_file_to_data_url(file_path)
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": build_system_prompt()},
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": build_prompt_for_image()},
                        {"type": "image_url", "image_url": {"url": data_url}},
                    ],
                },
            ],
            temperature=0.2,
            top_p=0.9,
            max_tokens=2048,
        )
        return (response.choices[0].message.content or "").strip()

    image_bytes = file_path.read_bytes()
    image_mime_type = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
        ".heic": "image/heic",
        ".heif": "image/heif",
    }.get(file_path.suffix.lower(), "image/png")

    response = client.models.generate_content(
        model=model_name,
        contents=[
            types_module.Part.from_bytes(data=image_bytes, mime_type=image_mime_type),
            build_prompt_for_image(),
        ],
    )
    return (response.text or "").strip()


def solve_with_retry(solver, retries: int, retry_base_seconds: float) -> str:
    last_error = None
    for attempt in range(1, retries + 1):
        try:
            return solver()
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            if attempt < retries:
                wait_seconds = min(retry_base_seconds * (2 ** (attempt - 1)), 20)
                print(f"[警告] 模型呼叫失敗，第 {attempt} 次重試前等待 {wait_seconds:.1f} 秒：{exc}")
                time.sleep(wait_seconds)
    raise RuntimeError(f"重試後仍失敗：{last_error}")


def main() -> None:
    load_dotenv()

    parser = argparse.ArgumentParser(description="使用 Gemma 或 Gemini 模型批次解題")
    parser.add_argument("--model", default="gemma-4-31b-it", help="模型名稱（預設：gemma-4-31b-it）")
    parser.add_argument(
        "--provider",
        choices=["auto", "hf", "gemini"],
        default="auto",
        help="API 來源：auto/hf/gemini（預設：auto）",
    )
    parser.add_argument("--input-dir", default="解題/un_solve_question", help="題目資料夾")
    parser.add_argument("--output-dir", default="解題/solve_question", help="答案輸出資料夾")
    parser.add_argument("--retries", type=int, default=3, help="每題重試次數")
    parser.add_argument("--retry-base-seconds", type=float, default=2.0, help="重試基礎等待秒數")
    parser.add_argument("--overwrite", action="store_true", help="覆蓋既有 md")
    args = parser.parse_args()

    provider, client, types_module = create_provider(args.model, args.provider)
    model_name = normalize_model_for_provider(args.model, provider)
    print(f"[資訊] 使用 provider={provider}，model={model_name}")

    input_dir = Path(args.input_dir).expanduser().resolve()
    output_dir = Path(args.output_dir).expanduser().resolve()

    if not input_dir.exists():
        raise FileNotFoundError(f"找不到輸入資料夾：{input_dir}")

    output_dir.mkdir(parents=True, exist_ok=True)

    files = sorted([p for p in input_dir.iterdir() if p.is_file()])
    if not files:
        print(f"[資訊] 沒有可解題檔案：{input_dir}")
        return

    solved_count = 0
    skipped_count = 0

    for file_path in files:
        ext = file_path.suffix.lower()
        if ext not in TEXT_EXTENSIONS and ext not in IMAGE_EXTENSIONS:
            print(f"[跳過] 不支援檔案格式：{file_path.name}")
            skipped_count += 1
            continue

        output_name = f"{sanitize_filename(file_path.stem)}.md"
        output_path = output_dir / output_name

        if output_path.exists() and not args.overwrite:
            print(f"[跳過] 已存在：{output_path.name}（可加 --overwrite）")
            skipped_count += 1
            continue

        print(f"[資訊] 正在解題：{file_path.name}")

        if ext in TEXT_EXTENSIONS:
            text = read_text_file(file_path)
            if not text:
                print(f"[跳過] 空白文字檔：{file_path.name}")
                skipped_count += 1
                continue

            answer_md = solve_with_retry(
                solver=lambda: solve_text_question(
                    provider=provider,
                    client=client,
                    types_module=types_module,
                    model_name=model_name,
                    text=text,
                ),
                retries=max(args.retries, 1),
                retry_base_seconds=max(args.retry_base_seconds, 0.2),
            )
        else:
            answer_md = solve_with_retry(
                solver=lambda: solve_image_question(
                    provider=provider,
                    client=client,
                    types_module=types_module,
                    model_name=model_name,
                    file_path=file_path,
                ),
                retries=max(args.retries, 1),
                retry_base_seconds=max(args.retry_base_seconds, 0.2),
            )

        output_path.write_text(answer_md + "\n", encoding="utf-8")
        print(f"[完成] {file_path.name} -> {output_path}")
        solved_count += 1

    print(f"[完成] 成功 {solved_count} 題，跳過 {skipped_count} 題。")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # noqa: BLE001
        print(f"[錯誤] {exc}")
