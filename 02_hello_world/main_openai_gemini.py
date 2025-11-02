from dotenv import dotenv_values
from openai import OpenAI

config = dotenv_values()
client = OpenAI(
    api_key=config["GEMINI_API_KEY"],
    base_url=config['GEMINI_BASE_URL'])

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Hello world!, Who are you?"

        }
    ]
)

print(response.choices[0].message)
print(response.model_dump_json(indent=2))
