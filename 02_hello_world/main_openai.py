from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant that helps people find information."},
    ]
)
print(response.choices[0].message.content)
print(response.model_dump_json(indent=2))


'''Output:
How can I assist you today?
{
    "id": "chatcmpl-CXVI418umpIngqeqxNv2P4WHzsS2T",
    "choices": [
        {
          "finish_reason": "stop",
          "index": 0,
          "logprobs": null,
          "message": {
              "content": "How can I assist you today?",
              "refusal": null,
              "role": "assistant",
              "annotations": [],
              "audio": null,
              "function_call": null,
              "tool_calls": null
          }
        }
    ],
    "created": 1762101140,
    "model": "gpt-4o-mini-2024-07-18",
    "object": "chat.completion",
    "service_tier": "default",
    "system_fingerprint": "fp_560af6e559",
    "usage": {
        "completion_tokens": 7,
        "prompt_tokens": 18,
        "total_tokens": 25,
        "completion_tokens_details": {
            "accepted_prediction_tokens": 0,
            "audio_tokens": 0,
            "reasoning_tokens": 0,
            "rejected_prediction_tokens": 0
        },
        "prompt_tokens_details": {
            "audio_tokens": 0,
            "cached_tokens": 0
        }
    }
}


'''

# curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent" \
#   - H 'Content-Type: application/json' \
#   - H 'X-goog-api-key: AIzaSyC1AK286n0KqCs03DGmrWRTySY0-PpAdqs' \
#   - X POST \
#   - d '{
#     "contents": [
#       {
#         "parts": [
#           {
#             "text": "Explain how AI works in a few words"
#           }
#         ]
#       }
#     ]
#   }'
