import openai
import os
from dotenv import dotenv_values
from groq import Groq

config = dotenv_values()

client = Groq(
    api_key=config["GROQ_API_KEY"],
    # base_url=config['GROQ_BASE_URL']
)
completion = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
          "role": "user",
            "content": "Hello world!, Who are you?"

        }
    ],
    temperature=1,
    max_completion_tokens=8192,
    top_p=1,
    reasoning_effort="medium",
    stream=True,
    stop=None
)

for chunk in completion:
    print(chunk.model_dump_json(indent=2))
    print(chunk.choices[0].delta, end='', flush=True)


# OpenAI API compatibility example

client = openai.OpenAI(
    base_url=config['GROQ_BASE_URL'],
    api_key=os.environ.get("GROQ_API_KEY")
)
