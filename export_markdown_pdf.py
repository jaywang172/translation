import argparse
import html
import re
import subprocess
from pathlib import Path

import markdown
from latex2mathml.converter import convert as latex_to_mathml


EDGE_CANDIDATES = [
    Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
    Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
]


def find_edge_executable(custom_path: str | None) -> Path:
    if custom_path:
        p = Path(custom_path).expanduser().resolve()
        if p.exists():
            return p
        raise FileNotFoundError(f"找不到指定的瀏覽器：{p}")

    for p in EDGE_CANDIDATES:
        if p.exists():
            return p

    raise FileNotFoundError(
        "找不到 msedge.exe。請安裝 Microsoft Edge，或用 --browser 指定瀏覽器路徑。"
    )


def math_token_to_html(tex: str, display: bool) -> str:
    source = tex.strip()
    if not source:
        return ""

    try:
        mathml = latex_to_mathml(source)
        if display:
            return f"<div class=\"math-display\">{mathml}</div>"
        return f"<span class=\"math-inline\">{mathml}</span>"
    except Exception:
        if display:
            fallback = html.escape(f"$${source}$$")
            return f"<pre class=\"math-fallback\">{fallback}</pre>"
        fallback = html.escape(f"${source}$")
        return f"<code class=\"math-fallback\">{fallback}</code>"


def preprocess_math_tokens(md_text: str) -> tuple[str, dict[str, str], dict[str, str]]:
    block_map: dict[str, str] = {}
    inline_map: dict[str, str] = {}

    block_index = 0

    def block_repl(match: re.Match[str]) -> str:
        nonlocal block_index
        token = f"MATHBLOCKTOKEN_{block_index}"
        block_index += 1
        block_map[token] = math_token_to_html(match.group(1), display=True)
        return f"\n\n{token}\n\n"

    processed = re.sub(r"\$\$(.+?)\$\$", block_repl, md_text, flags=re.DOTALL)

    inline_index = 0

    def inline_repl(match: re.Match[str]) -> str:
        nonlocal inline_index
        token = f"MATHINLINETOKEN_{inline_index}"
        inline_index += 1
        inline_map[token] = math_token_to_html(match.group(1), display=False)
        return token

    processed = re.sub(
        r"(?<!\\)\$(?!\$)([^\n$]+?)(?<!\\)\$(?!\$)",
        inline_repl,
        processed,
    )

    return processed, block_map, inline_map


def markdown_to_html(md_text: str, title: str) -> str:
    processed_text, block_map, inline_map = preprocess_math_tokens(md_text)

    body = markdown.markdown(
        processed_text,
        extensions=[
            "extra",
            "sane_lists",
        ],
    )

    for token, html_snippet in block_map.items():
        body = body.replace(f"<p>{token}</p>", html_snippet)
        body = body.replace(token, html_snippet)

    for token, html_snippet in inline_map.items():
        body = body.replace(token, html_snippet)

    return f"""<!doctype html>
<html lang=\"zh-Hant\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>{title}</title>
  <style>
    @page {{ size: A4; margin: 16mm; }}
    body {{
      font-family: "Microsoft JhengHei", "Noto Sans CJK TC", "Segoe UI", sans-serif;
      line-height: 1.62;
      color: #111;
      font-size: 14px;
      overflow-wrap: break-word;
    }}
    h1, h2, h3, h4, h5, h6 {{
      page-break-after: avoid;
      margin-top: 1.1em;
      margin-bottom: 0.45em;
      line-height: 1.35;
    }}
    h1 {{ font-size: 1.6rem; }}
    h2 {{ font-size: 1.32rem; }}
    h3 {{ font-size: 1.12rem; }}
    p, li, blockquote {{ margin: 0.42em 0; }}
    img {{
      max-width: 100%;
      height: auto;
      display: block;
      margin: 10px 0 14px;
      break-inside: avoid;
    }}
    hr {{ border: 0; border-top: 1px solid #bbb; margin: 16px 0; }}
    pre, code {{
      font-family: "Consolas", "Cascadia Mono", monospace;
      white-space: pre-wrap;
      word-break: break-word;
    }}
    .math-inline math {{ font-size: 1em; vertical-align: middle; }}
    .math-display {{ margin: 0.5em 0; }}
    .math-display math {{ display: block; text-align: left; }}
    .math-fallback {{
      color: #333;
      background: #f7f7f7;
      border-radius: 4px;
      padding: 2px 6px;
    }}
  </style>
</head>
<body>
{body}
</body>
</html>
"""


def export_markdown_to_pdf(md_path: Path, pdf_path: Path, browser_path: str | None) -> None:
    md_text = md_path.read_text(encoding="utf-8", errors="ignore")
    html_text = markdown_to_html(md_text, md_path.stem)

    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    temp_html = pdf_path.with_suffix(".render.html")
    temp_html.write_text(html_text, encoding="utf-8")

    browser = find_edge_executable(browser_path)

    cmd = [
        str(browser),
        "--headless",
        "--disable-gpu",
        "--allow-file-access-from-files",
        "--run-all-compositor-stages-before-draw",
        "--virtual-time-budget=25000",
        "--print-to-pdf-no-header",
        f"--print-to-pdf={pdf_path}",
        temp_html.resolve().as_uri(),
    ]
    subprocess.run(cmd, check=True)

    temp_html.unlink(missing_ok=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="把 Markdown（含圖片與數學式）匯出成 PDF（離線 MathML）")
    parser.add_argument("--input", required=True, help="輸入 Markdown 路徑")
    parser.add_argument("--output", required=True, help="輸出 PDF 路徑")
    parser.add_argument("--browser", default=None, help="瀏覽器執行檔路徑（可省略，預設自動找 Edge）")
    args = parser.parse_args()

    md_path = Path(args.input).expanduser().resolve()
    pdf_path = Path(args.output).expanduser().resolve()

    if not md_path.exists():
        raise FileNotFoundError(f"找不到輸入檔：{md_path}")

    export_markdown_to_pdf(md_path, pdf_path, args.browser)
    print(f"[完成] PDF 輸出：{pdf_path}")


if __name__ == "__main__":
    main()
