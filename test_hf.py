import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Load .env
load_dotenv()

# Get Hugging Face token
hf_token = os.getenv("HF_TOKEN")

if not hf_token:
    print("❌ HF_TOKEN not found in .env")
    raise SystemExit

# Create Hugging Face client
client = InferenceClient(
    api_key=hf_token
)

# Test the LLM
response = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3-0324",
    messages=[
        {
            "role": "user",
            "content": "Explain overfitting in one simple sentence."
        }
    ],
    max_tokens=100
)

print("\n✅ Hugging Face LLM is working!")
print("\nAI Response:")
print(response.choices[0].message.content)