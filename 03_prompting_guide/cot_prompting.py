from openai.types.chat import ChatCompletionMessageParam
import json

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


SYSTEM_PROMPT = """
    You're an expert AI Assistant in resolving user queries using chain of thought.
    You work on START, PLAN and OUPUT steps.
    You need to first PLAN what needs to be done. The PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUTPUT.

    Rules:
    - Strictly Follow the given JSON output format
    - Only run one step at a time.
    - The sequence of steps is START (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT (which is going to the displayed to the user).

    Output JSON Format:
    { "step": "START" | "PLAN" | "OUTPUT", "content": "string" }

    Example:
    START: Hey, Can you solve 2 + 3 * 5 / 10
    PLAN: { "step": "PLAN": "content": "Seems like user is interested in math problem" }
    PLAN: { "step": "PLAN": "content": "looking at the problem, we should solve this using BODMAS method" }
    PLAN: { "step": "PLAN": "content": "Yes, The BODMAS is correct thing to be done here" }
    PLAN: { "step": "PLAN": "content": "first we must multiply 3 * 5 which is 15" }
    PLAN: { "step": "PLAN": "content": "Now the new equation is 2 + 15 / 10" }
    PLAN: { "step": "PLAN": "content": "We must perform divide that is 15 / 10  = 1.5" }
    PLAN: { "step": "PLAN": "content": "Now the new equation is 2 + 1.5" }
    PLAN: { "step": "PLAN": "content": "Now finally lets perform the add 3.5" }
    PLAN: { "step": "PLAN": "content": "Great, we have solved and finally left with 3.5 as ans" }
    OUTPUT: { "step": "OUTPUT": "content": "3.5" }
"""

print("\n\n\n")


system_message: ChatCompletionSystemMessageParam = {
    "role": "system",
    "content": SYSTEM_PROMPT
}

user_message: ChatCompletionUserMessageParam = {
    "role": "user",
    "content": "your prompt here"
}


message_history: list = [
    system_message
]

user_query = input("👉🏻 ")
message_history.append(user_message)

while True:
    response = client.chat.completions.create(
        model="gpt-4o",
        response_format={"type": "json_object"},
        messages=message_history
    )

    raw_result = response.choices[0].message.content
    message_history.append({"role": "assistant", "content": raw_result})

    parsed_result = json.loads(raw_result)

    if parsed_result.get("step") == "START":
        print("🔥", parsed_result.get("content"))
        continue

    if parsed_result.get("step") == "PLAN":
        print("🧠", parsed_result.get("content"))
        continue

    if parsed_result.get("step") == "OUTPUT":
        print("🤖", parsed_result.get("content"))
        break

print("\n\n\n")


response = client.chat.completions.create(
    model=model,
    messages=[
        system_message,
        user_message
    ]
)

print(response.choices[0].message.content)
# print(response.model_dump_json(indent=2))
