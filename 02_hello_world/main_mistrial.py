from openai import OpenAI
from mistralai import Mistral
from dotenv import dotenv_values

config = dotenv_values()


# with Mistral(
#     api_key=config["MISTRAL_API_KEY"]
# ) as mistral:

#     res = mistral.chat.complete(model="mistral-small-latest", messages=[
#         {
#             "content": "Who is the best French painter? Answer in one short sentence.",
#             "role": "user",
#         },
#     ], stream=False)

#     # Handle response
#     print(res.choices[0].message)
#     print(res.model_dump_json(indent=2))


#

client = OpenAI(
    api_key=config["MISTRAL_API_KEY"],
    base_url=config['MISTRAL_BASE_URL'])

response = client.chat.completions.create(
    model="mistral-small-latest",
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
