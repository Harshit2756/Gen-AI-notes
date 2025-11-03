from dotenv import dotenv_values, load_dotenv
from openai import OpenAI
from openai.types.chat import (ChatCompletionSystemMessageParam,
                               ChatCompletionUserMessageParam)

# =================================== API SETUP ===================================
load_dotenv()
config = dotenv_values()

api_key = config["GEMINI_API_KEY"]
base_url = config['GEMINI_BASE_URL']

model = "gemini-2.5-flash"

client = OpenAI(
    api_key=api_key,
    base_url=base_url
)

print(f"{"="*30} API INFO {"="*40}")
print(f"Base URL: {base_url}")
print(f"Model: {model}")
print(f"{"="*70}")
print()


# =================================================================================


# Few Shot Prompting: Directly giving the inst to the model and few examples to the model
SYSTEM_PROMPT = """
You should only and only ans the coding related questions. Do not ans anything else. Your name is Alexa. If user asks something other than coding, just say sorry.

Rule:
- Strictly follow the output in JSON format

Output Format:
{{
 "code": "string" or null,
 "isCodingQuestion": boolean
}}

Examples:
Q: Can you explain the a + b whole square?
A: {{ "code": null, "isCodingQuestion": false }}

Q: Hey, Write a code in python for adding two numbers.
A: {{ "code": "def add(a, b):
        return a + b", "isCodingQuestion": false }}
"""

system_message: ChatCompletionSystemMessageParam = {
    "role": "system",
    "content": SYSTEM_PROMPT
}

user_message: ChatCompletionUserMessageParam = {
    "role": "user",
    "content": "your prompt here"
}

response = client.chat.completions.create(
    model=model,
    messages=[
        system_message,
        user_message
    ]
)

print(response.choices[0].message.content)
# print(response.model_dump_json(indent=2))
