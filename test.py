# from openai import OpenAI

# client = OpenAI(
#   base_url = "https://integrate.api.nvidia.com/v1",
#   api_key = "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"
# )

# completion = client.chat.completions.create(
#   model="zai-org/GLM-4.7",
#   messages=[{"role":"user","content":"寫一段快速排序法 Python 代碼"}],
#   temperature=0.5,
#   top_p=0.7,
#   max_tokens=1024,
#   stream=True
# )

# for chunk in completion:
#   if chunk.choices[0].delta.content is not None:
#     print(chunk.choices[0].delta.content, end="")

from openai import OpenAI

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = "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"
)

# 根據官方說明，推薦設定為 temp=1.0, top_p=0.95
completion = client.chat.completions.create(
  model="minimaxai/minimax-m2.7", 
  messages=[{"role":"user","content":"我有一段生產環境的 Log 出現 500 錯誤，請幫我分析可能原因：(貼上你的Log)"}],
  temperature=1.0,
  top_p=0.95,
  max_tokens=2048,
  stream=True
)

for chunk in completion:
    # 增加這行判斷：確保 choices 不是空的
    if chunk.choices:
        content = chunk.choices[0].delta.content
        if content is not None:
            print(content, end="", flush=True)


