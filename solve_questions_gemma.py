import argparse
import base64
import os
import re
import time
from pathlib import Path

from dotenv import load_dotenv
from huggingface_hub import InferenceClient


TEXT_EXTENSIONS = {".txt", ".md"}
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".bmp"}


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
        ".bmp": "image/bmp",
    }
    mime_type = mime_map.get(ext, "application/octet-stream")
    b64 = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime_type};base64,{b64}"


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


def solve_text_question(
    client: InferenceClient,
    model: str,
    question_text: str,
    max_tokens: int,
) -> str:
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": build_system_prompt()},
            {
                "role": "user",
                "content": (
                    "請解以下線性代數題目。\n\n"
                    "[題目原文開始]\n"
                    f"{question_text}\n"
                    "[題目原文結束]"
                ),
            },
        ],
        temperature=0.2,
        top_p=0.9,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content.strip()


def solve_image_question(
    client: InferenceClient,
    model: str,
    image_path: Path,
    max_tokens: int,
) -> str:
    data_url = image_file_to_data_url(image_path)
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": build_system_prompt()},
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "請讀取這張題目圖片後解題。"},
                    {"type": "image_url", "image_url": {"url": data_url}},
                ],
            },
        ],
        temperature=0.2,
        top_p=0.9,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content.strip()


def solve_with_retry(
    solver,
    retries: int,
    retry_base_seconds: float,
):
    last_error = None
    for attempt in range(1, retries + 1):
        try:
            return solver()
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            if attempt < retries:
                wait_seconds = min(retry_base_seconds * (2 ** (attempt - 1)), 20)
                print(f"[警告] 呼叫模型失敗，第 {attempt} 次重試前等待 {wait_seconds:.1f} 秒：{exc}")
                time.sleep(wait_seconds)

    raise RuntimeError(f"重試後仍失敗：{last_error}")


def main() -> None:
    load_dotenv()

    parser = argparse.ArgumentParser(description="使用 Gemma 4 31B 批次解 un_solve_question 題目")
    parser.add_argument(
        "--model",
        default="google/gemma-4-31b-it",
        help="Hugging Face 模型 ID（預設：google/gemma-4-31b-it）",
    )
    parser.add_argument(
        "--input-dir",
        default="解題/un_solve_question",
        help="未解題目資料夾（預設：解題/un_solve_question）",
    )
    parser.add_argument(
        "--output-dir",
        default="解題/solve_question",
        help="解答輸出資料夾（預設：解題/solve_question）",
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=2048,
        help="每題最大輸出 token（預設：2048）",
    )
    parser.add_argument(
        "--retries",
        type=int,
        default=3,
        help="每題重試次數（預設：3）",
    )
    parser.add_argument(
        "--retry-base-seconds",
        type=float,
        default=2.0,
        help="重試基礎等待秒數（預設：2.0）",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="覆蓋既有輸出檔（預設：不覆蓋）",
    )

    args = parser.parse_args()

    api_key = os.environ.get("HF_TOKEN") or os.environ.get("HUGGINGFACEHUB_API_TOKEN")
    if not api_key:
        raise EnvironmentError("找不到 HF_TOKEN，請先在 .env 或環境變數設定 Hugging Face Token")

    input_dir = Path(args.input_dir).expanduser().resolve()
    output_dir = Path(args.output_dir).expanduser().resolve()

    if not input_dir.exists():
        raise FileNotFoundError(f"找不到輸入資料夾：{input_dir}")

    output_dir.mkdir(parents=True, exist_ok=True)

    client = InferenceClient(api_key=api_key)

    files = sorted([p for p in input_dir.iterdir() if p.is_file()])
    if not files:
        print(f"[資訊] 輸入資料夾沒有檔案：{input_dir}")
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
            print(f"[跳過] 已存在：{output_path.name}（可加 --overwrite 覆蓋）")
            skipped_count += 1
            continue

        print(f"[資訊] 正在解題：{file_path.name}")

        if ext in TEXT_EXTENSIONS:
            question_text = read_text_file(file_path)
            if not question_text:
                print(f"[跳過] 空白文字檔：{file_path.name}")
                skipped_count += 1
                continue

            answer_md = solve_with_retry(
                solver=lambda: solve_text_question(
                    client=client,
                    model=args.model,
                    question_text=question_text,
                    max_tokens=args.max_tokens,
                ),
                retries=max(args.retries, 1),
                retry_base_seconds=max(args.retry_base_seconds, 0.2),
            )
        else:
            answer_md = solve_with_retry(
                solver=lambda: solve_image_question(
                    client=client,
                    model=args.model,
                    image_path=file_path,
                    max_tokens=args.max_tokens,
                ),
                retries=max(args.retries, 1),
                retry_base_seconds=max(args.retry_base_seconds, 0.2),
            )

        output_path.write_text(answer_md + "\n", encoding="utf-8")
        print(f"[完成] {file_path.name} -> {output_path}")
        solved_count += 1

    print(f"[完成] 解題完成，成功 {solved_count} 題，跳過 {skipped_count} 題。")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # noqa: BLE001
        print(f"[錯誤] {exc}")
