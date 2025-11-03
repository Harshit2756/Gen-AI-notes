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

print(f"{"="*20} API INFO {"="*20}")
print(f"Base URL: {base_url}")
print(f"Model: {model}")
print(f"{"="*50}")
print()


# =================================================================================

# Zero short prompting example (Asking the model to complete a task with no prior examples.)
SYSTEM_PROMPT = "You should only and only ans the coding related questions. Do not ans anything else. If user asks something other than coding, just say sorry."
system_message: ChatCompletionSystemMessageParam = {
    "role": "system",
    "content": SYSTEM_PROMPT
}

user_message: ChatCompletionUserMessageParam = {
    "role": "user",
    # here the model returns a  anser 
    # "content": "Hey can you tell me how a+b the whole square is solved?"
    # here the model refuses to answer as per the system prompt
    "content": "Can you explain the theory of relativity?"
    
}


response = client.chat.completions.create(
    model=model, messages=[system_message, user_message])

print(response.choices[0].message.content)
# print(response.model_dump_json(indent=2))
