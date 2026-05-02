# Gemini 多模態 PDF 逐頁翻譯

使用 Google Gemini API 將 PDF 逐頁翻譯為繁體中文（或指定語言），並輸出：

- 每頁一個 `.md`
- 一個整合好的 `.translated.md`

## 功能特色

- 影像直送模型（不依賴 OCR）
- 自動偵測圖表頁並提高 DPI
- 斷點續跑（`--resume`）
- 429/503 自動等待重試與備援模型

## 安裝

```powershell
pip install -r requirements.txt
```

## 設定 Gemini API Key

建議使用 `.env` 或環境變數，不要寫死在程式：

```powershell
$env:GEMINI_API_KEY="你的 Google API Key"
```

## 使用方式

1) 先做小範圍測試

```powershell
python .\translate_pdf_gemini.py --pdf ".\linear-algebra-author-gilbert-strang.pdf" --start-page 1 --end-page 3 --auto-chart-dpi
```

2) 翻譯整本（推薦）

```powershell
python .\translate_pdf_gemini.py --pdf ".\linear-algebra-author-gilbert-strang.pdf" --model "gemma-4-31b-it" --target-lang "繁體中文" --auto-chart-dpi --vision-dpi 240 --vision-high-dpi 360
```

3) 遇到額度限制時續跑與備援模型

```powershell
python .\translate_pdf_gemini.py --pdf ".\linear-algebra-author-gilbert-strang.pdf" --model "gemma-4-31b-it" --target-lang "繁體中文" --auto-chart-dpi --vision-dpi 240 --vision-high-dpi 360 --resume --retries-per-model 4 --fallback-models "gemini-2.0-flash,gemini-1.5-flash"
```

## 輸出位置

預設在 `translations/`：

- `檔名.page-0001.md`
- `檔名.page-0002.md`
- ...
- `檔名.translated.md`

## 注意事項

1. 請勿將 `.env` 推到 GitHub。
2. 圖表多、字小的頁面建議啟用 `--auto-chart-dpi` 並提高 `--vision-high-dpi`。
