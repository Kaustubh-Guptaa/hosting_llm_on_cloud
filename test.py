# # Test: vLLM model server

# from openai import OpenAI

# client = OpenAI(
#     base_url="http://localhost:1207/v1",
#     api_key="EMPTY"  
# )

# response = client.chat.completions.create(
#     model="microsoft/Phi-4-mini-instruct",
#     messages=[
#         {
#             "role": "user", 
#             "content": "What is Hugging Face?"
#         }
#     ],
#     max_tokens=50
# )

# print(response.choices[0].message.content)

# # -------------------------------------------------

# # Test: FastAPI server

import requests

response = requests.post(
    "http://localhost:2088/inference",
    json={
        "prompt": "hello"
    }
)

print(response.json())