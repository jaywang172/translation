import argparse
import re
from pathlib import Path


IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".heic", ".heif", ".bmp"}

SECTIONS = [
    ("3.1 小節", [5, 9, 14, 17, 19, 20, 22, 25, 26, 27]),
    ("3.2 小節", [1, 2, 5, 11, 17, 24, 29, 46]),
    ("3.3 小節", [1, 3, 4, 18, 19, 30, 32]),
    ("3.4 小節", [1, 2, 13, 16, 18, 23, 29, 38]),
    ("Chapter 1-1", [1, 4, 15, 25]),
    ("Chapter 1-2", [1, 3, 7, 8, 13]),
    ("Chapter 1-3", [1, 2, 4, 7]),
    ("Chapter 2-1", [2, 5, 12, 13, 18, 19, 27]),
    ("Chapter 2-2", [5, 9, 12, 19, 27]),
    ("Chapter 2-3", [3, 12, 14, 25, 27]),
    ("Chapter 2-4", [7, 12, 15, 19, 26, 28, 29]),
    ("Chapter 2-5", [1, 5, 8, 10, 15, 23, 27]),
    ("Chapter 2-6", [5, 6, 16]),
    ("Chapter 2-7", [1, 11, 17, 20, 22]),
]


def sanitize_filename(name: str) -> str:
    safe = re.sub(r"[^\w\-.]+", "_", name, flags=re.UNICODE)
    return safe.strip("_") or "question"


def heading_shift(md_text: str, shift: int = 2) -> str:
    lines = md_text.splitlines()
    result = []
    for line in lines:
        m = re.match(r"^(#{1,6})(\s+.*)$", line)
        if not m:
            result.append(line)
            continue
        new_level = min(6, len(m.group(1)) + shift)
        result.append("#" * new_level + m.group(2))
    return "\n".join(result).strip()


def gather_solutions(solution_dir: Path) -> list[Path]:
    files = []
    for p in solution_dir.glob("*.md"):
        if p.name.startswith("螢幕擷取畫面_"):
            files.append(p)
    return sorted(files, key=lambda x: x.name)


def build_image_map(image_dir: Path) -> dict[str, Path]:
    result: dict[str, Path] = {}
    for p in image_dir.iterdir():
        if not p.is_file():
            continue
        if p.suffix.lower() not in IMAGE_EXTENSIONS:
            continue
        result[sanitize_filename(p.stem)] = p
    return result


def md_rel_path(from_file: Path, target_file: Path) -> str:
    return str(target_file.relative_to(from_file.parent.parent) if False else Path(
        __import__("os").path.relpath(str(target_file), str(from_file.parent))
    )).replace("\\", "/")


def problem_block(problem_no: int, image_path: Path | None, solution_path: Path, output_file: Path) -> str:
    content = solution_path.read_text(encoding="utf-8", errors="ignore")
    content = heading_shift(content, shift=2)

    if image_path is not None:
        img_rel = md_rel_path(output_file, image_path)
        image_part = f"### 圖片\n\n![{image_path.name}]({img_rel})\n"
    else:
        image_part = "### 圖片\n\n（找不到對應圖片）\n"

    return (
        f"## Problem {problem_no}\n\n"
        f"{image_part}\n"
        "### 解題\n\n"
        f"{content}\n\n"
        "---\n"
    )


def chapter_filename(title: str) -> str:
    mapping = {
        "3.1 小節": "section_3_1.md",
        "3.2 小節": "section_3_2.md",
        "3.3 小節": "section_3_3.md",
        "3.4 小節": "section_3_4.md",
        "Chapter 1-1": "chapter_1_1.md",
        "Chapter 1-2": "chapter_1_2.md",
        "Chapter 1-3": "chapter_1_3.md",
        "Chapter 2-1": "chapter_2_1.md",
        "Chapter 2-2": "chapter_2_2.md",
        "Chapter 2-3": "chapter_2_3.md",
        "Chapter 2-4": "chapter_2_4.md",
        "Chapter 2-5": "chapter_2_5.md",
        "Chapter 2-6": "chapter_2_6.md",
        "Chapter 2-7": "chapter_2_7.md",
    }
    return mapping.get(title, sanitize_filename(title) + ".md")


def main() -> None:
    parser = argparse.ArgumentParser(description="把解題結果整理成章節總整理 Markdown")
    parser.add_argument("--solution-dir", default="解題/solve_question", help="已解答 md 資料夾")
    parser.add_argument("--image-dir", default="解題/un_solve_question", help="題目圖片資料夾")
    parser.add_argument("--master-output", default="解題/solve_question/總整理_超大.md", help="超大總整理輸出路徑")
    parser.add_argument("--chapters-dir", default="解題/solve_question/章節分開", help="章節分開輸出資料夾")
    args = parser.parse_args()

    solution_dir = Path(args.solution_dir).expanduser().resolve()
    image_dir = Path(args.image_dir).expanduser().resolve()
    master_output = Path(args.master_output).expanduser().resolve()
    chapters_dir = Path(args.chapters_dir).expanduser().resolve()

    if not solution_dir.exists():
        raise FileNotFoundError(f"找不到 solution 資料夾：{solution_dir}")
    if not image_dir.exists():
        raise FileNotFoundError(f"找不到 image 資料夾：{image_dir}")

    solution_files = gather_solutions(solution_dir)
    if not solution_files:
        raise RuntimeError("找不到可整理的解答檔（預期為 螢幕擷取畫面_*.md）")

    image_map = build_image_map(image_dir)

    requested_count = sum(len(problems) for _, problems in SECTIONS)
    if requested_count > len(solution_files):
        raise RuntimeError(
            f"章節需求共 {requested_count} 題，但目前只有 {len(solution_files)} 份解答。"
        )

    chapters_dir.mkdir(parents=True, exist_ok=True)
    master_output.parent.mkdir(parents=True, exist_ok=True)

    pointer = 0
    master_parts: list[str] = [
        "# 線性代數解題總整理（超大版）\n",
        "此檔依你指定的章節與題號順序整理。每題排版為：圖片 -> 解題。\n",
    ]

    for chapter_title, problem_list in SECTIONS:
        chapter_parts: list[str] = [f"# {chapter_title}\n"]
        master_parts.append(f"\n# {chapter_title}\n")

        for problem_no in problem_list:
            solution_path = solution_files[pointer]
            pointer += 1

            key = sanitize_filename(solution_path.stem)
            image_path = image_map.get(key)
            block = problem_block(problem_no, image_path, solution_path, master_output)

            chapter_parts.append(block)
            master_parts.append(block)

        chapter_path = chapters_dir / chapter_filename(chapter_title)
        chapter_path.write_text("\n".join(chapter_parts).strip() + "\n", encoding="utf-8")

    leftovers = solution_files[pointer:]
    if leftovers:
        master_parts.append("\n# 未分配題目\n")
        for i, solution_path in enumerate(leftovers, start=1):
            key = sanitize_filename(solution_path.stem)
            image_path = image_map.get(key)
            block = problem_block(i, image_path, solution_path, master_output)
            master_parts.append(block)

    master_output.write_text("\n".join(master_parts).strip() + "\n", encoding="utf-8")

    print(f"[完成] 總整理：{master_output}")
    print(f"[完成] 章節分開：{chapters_dir}")
    print(f"[資訊] 使用解答數：{pointer} / 全部 {len(solution_files)}")
    print(f"[資訊] 未分配：{len(leftovers)}")


if __name__ == "__main__":
    main()
