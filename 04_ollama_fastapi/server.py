from ollama import Client

from fastapi import FastAPI, Body

app = FastAPI()
client = Client(
    host="http://localhost:11434",
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/contact-us")
def contact_us():
    return {"email": "Harshit.khandelwal@gmail.com"}


@app.post("/chat")
def chat(
    message: str = Body(..., description="The message to send to the model"),
): 
    response = client.chat(model="gemma3", messages=[
                {"role": "user", "content": message}])
    return {"response": response.message.content}