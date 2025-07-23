import json
import re
from openai import OpenAI
from app.core.config import settings

openai_client = OpenAI(api_key=settings.OPENAI_API_KEY)

def ai_prompt(input_text):
    prompt = f"""
        請分析這段內容的營養成分，並回傳 JSON 格式：
        格式：
        {{
        "food_name": "...",
        "calories": ...,
        "protein": ...,
        "carbs": ...,
        "fat": ...
        }}
        食物內容：{input_text}
        """
    return prompt

def extract_json_from_text(text: str):
    match = re.search(r"```json\s*(\{.*?\})\s*```", text, re.DOTALL)
    if not match:
        raise ValueError("找不到 JSON 區塊")
    return json.loads(match.group(1))

def log_food_with_ai(input_text):
    completion = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": ai_prompt(input_text)}],
        # response_format="json"
    )

    content = completion.choices[0].message.content
    print("AI 回應內容：\n", content)
    nutrition_data = extract_json_from_text(content)
    print(nutrition_data)
    return nutrition_data

# log_food_with_ai("全麥吐司兩片加一匙果醬")