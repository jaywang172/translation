# Gemma 31B 逐頁翻譯 PDF（Hugging Face API）

這個工具可把 PDF 逐頁翻譯成繁體中文（或你指定的語言），並輸出：

- 每頁一個 `.md` 檔
- 一個整合好的 `.translated.md`

> 已預設模型：`google/gemma-4-31b-it`

## 1) 安裝

```powershell
pip install -r requirements.txt
```

## 2) 設定 API Token（請用環境變數，不要寫死在程式）

```powershell
$env:HF_TOKEN="你的 Hugging Face Token"
```

## 3) 執行逐頁翻譯

```powershell
python .\translate_pdf_gemma.py --pdf ".\linear-algebra-author-gilbert-strang.pdf"
```

> Gemma 預設優先順序已設定為：
> 1. `google/gemma-4-26b-it`（第一優先）
> 2. `google/gemma-4-31b-it`（第二優先，備援）

## 用 Google Gemini API 直接看頁面影像翻譯（推薦）

這個模式不依賴 OCR 文字抽取，會直接把每頁渲染成圖片傳給 Gemini。

1) 設定 Gemini API Key

```powershell
$env:GEMINI_API_KEY="你的 Google API Key"
```

2) 先做 dry-run 測試（不打 API）

```powershell
python .\translate_pdf_gemini.py --pdf ".\linear-algebra-author-gilbert-strang.pdf" --dry-run --start-page 1 --end-page 3 --auto-chart-dpi
```

3) 跑完整本繁中翻譯（圖表頁自動高 DPI）

```powershell
python .\translate_pdf_gemini.py --pdf ".\linear-algebra-author-gilbert-strang.pdf" --target-lang "繁體中文" --auto-chart-dpi --vision-dpi 240 --vision-high-dpi 360
```

4) 若遇到 429/503（額度或尖峰），用續跑與備援模型

```powershell
python .\translate_pdf_gemini.py --pdf ".\linear-algebra-author-gilbert-strang.pdf" --target-lang "繁體中文" --auto-chart-dpi --vision-dpi 240 --vision-high-dpi 360 --resume --retries-per-model 4 --fallback-models "gemini-2.0-flash,gemini-1.5-flash"
```

說明：
- `--resume`：已完成頁面會自動跳過，從失敗頁接著跑。
- 程式會嘗試解析 API 建議的 `retryDelay`，比固定退避更穩定。
- 跑完會自動重建 `translated.md`，把現有頁面整併起來。

> 預設已啟用 `--ocr-mode on-empty`，當頁面抓不到文字時會自動 OCR。
>
> OCR 後端使用 Tesseract，Windows 若未安裝請先安裝（可用 winget/choco），
> 或在執行時用 `--tesseract-cmd` 指定 `tesseract.exe` 完整路徑。

## 常用選項

- 只翻指定頁碼區間：

```powershell
python .\translate_pdf_gemma.py --pdf ".\linear-algebra-author-gilbert-strang.pdf" --start-page 1 --end-page 5
```

- 改目標語言：

```powershell
python .\translate_pdf_gemma.py --pdf ".\linear-algebra-author-gilbert-strang.pdf" --target-lang "英文"
```

- 僅測試 PDF 文字抽取（不呼叫模型）：

```powershell
python .\translate_pdf_gemma.py --pdf ".\linear-algebra-author-gilbert-strang.pdf" --extract-only --start-page 1 --end-page 1
```

- 強制每頁都用 OCR（適合整份掃描 PDF）：

```powershell
python .\translate_pdf_gemma.py --pdf ".\linear-algebra-author-gilbert-strang.pdf" --ocr-mode all
```

- 指定模型優先順序（26B A4B -> 31B）：

```powershell
python .\translate_pdf_gemma.py --pdf ".\linear-algebra-author-gilbert-strang.pdf" --model "google/gemma-4-26b-it" --fallback-models "google/gemma-4-31b-it"
```

- 調整 OCR 精度（提高 DPI）：

```powershell
python .\translate_pdf_gemma.py --pdf ".\linear-algebra-author-gilbert-strang.pdf" --ocr-mode on-empty --ocr-dpi 300
```

- 遇到圖表頁自動提高 DPI（建議翻教科書/投影片）：

```powershell
python .\translate_pdf_gemma.py --pdf ".\linear-algebra-author-gilbert-strang.pdf" --ocr-mode on-empty --auto-chart-dpi --ocr-dpi 240 --ocr-high-dpi 360
```

- 指定 Tesseract 執行檔（未加入 PATH 時）：

```powershell
python .\translate_pdf_gemma.py --pdf ".\linear-algebra-author-gilbert-strang.pdf" --ocr-mode all --tesseract-cmd "C:\Program Files\Tesseract-OCR\tesseract.exe"
```

## 輸出位置

預設在 `translations/`：

- `檔名.page-0001.md`
- `檔名.page-0002.md`
- ...
- `檔名.translated.md`

## 注意事項

1. 若某頁是掃描影像，純文字擷取可能為空；本工具可用 `--ocr-mode` 自動補 OCR。
2. 大頁面可能超過輸出 token，必要時提高 `--max-new-tokens` 或拆頁段。
3. 請務必保護 API Token，不要上傳到 Git 或公開貼文。
4. 圖表很多但字很小時，可開 `--auto-chart-dpi` 並提高 `--ocr-high-dpi`（如 360~420）。

## 用 Gemma 4 31B 批次解題（un_solve_question -> solve_question）

這個模式會掃描 `解題/un_solve_question` 的題目檔，並把解答輸出成 `.md` 到 `解題/solve_question`。

支援題目格式：
- 文字：`.txt`, `.md`
- 圖片：`.png`, `.jpg`, `.jpeg`, `.webp`, `.bmp`

每一份輸出都會固定包含三段：
- `# 題目復述`
- `# 解題過程`
- `# 用到的觀念`

1) 設定 Hugging Face Token

```powershell
$env:HF_TOKEN="你的 Hugging Face Token"
```

2) 執行批次解題（預設模型：`google/gemma-4-31b-it`）

```powershell
python .\solve_questions_gemma.py
```

3) 常用參數

```powershell
# 覆蓋既有輸出
python .\solve_questions_gemma.py --overwrite

# 指定模型與輸入輸出資料夾
python .\solve_questions_gemma.py --model "google/gemma-4-31b-it" --input-dir "解題/un_solve_question" --output-dir "解題/solve_question"
```

## 用 GEMINI API KEY 批次解題（un_solve_question -> solve_question）

`solve_questions_gemini.py` 會優先使用 Gemini API Key，預設模型是 `gemma-4-31b-it`，可直接避開 `gemini-2.5-flash` 的配額上限。

也支援改用 Hugging Face（`--provider hf`）。

1) 設定金鑰

```powershell
# 建議：用 Gemini API Key 跑 Gemma
$env:GEMINI_API_KEY="你的 Gemini API Key"

# 若要改走 Hugging Face 才需要
$env:HF_TOKEN="你的 Hugging Face Token"
```

2) 執行（預設模型：`gemma-4-31b-it`）

```powershell
python .\solve_questions_gemini.py
```

3) 常用參數

```powershell
# 覆蓋已存在答案
python .\solve_questions_gemini.py --overwrite

# 指定 Gemini 模型
python .\solve_questions_gemini.py --model "gemini-2.5-flash" --provider gemini

# 指定 Gemma 4 31B（走 Gemini API）
python .\solve_questions_gemini.py --model "gemma-4-31b-it" --provider gemini

# 指定 Gemma 4 31B（走 Hugging Face）
python .\solve_questions_gemini.py --model "google/gemma-4-31b-it" --provider hf
```
