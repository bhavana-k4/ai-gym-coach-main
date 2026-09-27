from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

print("API KEY FOUND:", bool(api_key))

client = Groq(api_key=api_key)

print("Testing GPT-OSS 120B...")

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": "Say hello in one short sentence."
        }
    ],
    temperature=0.4
)

print("SUCCESS!")
print("MODEL RESPONSE:")
print(response.choices[0].message.content)