import anthropic
from dotenv import dotenv_values

config = dotenv_values()

client = anthropic.Anthropic(
    api_key=config["ANTHROPIC_API_KEY"],
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude"}
    ]
)
print(message.content)
print(message.model_dump_json(indent=2))