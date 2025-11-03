from dotenv import dotenv_values, load_dotenv
from google import genai
from openai import OpenAI

load_dotenv()
# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

response = client.models.generate_content(  # type: ignore

    model="gemini-2.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)

# OpenAI Gemini equivalent


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
