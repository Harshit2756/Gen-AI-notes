import requests
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()


def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"

    return "Something went wrong"


def main():
    user_query = input("> ")

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": user_query}
        ]
    )

    print(f"🤖: {response.choices[0].message.content}")


print(
    f"🚀 Weather Agent is running... Type your query below. {get_weather("delhi")}")
# main()
