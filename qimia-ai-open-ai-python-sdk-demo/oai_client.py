from openai import OpenAI

API_URL = "https://api.qimiaai.com"
API_KEY = "your_api_key_here"  # Your valid Qimia AI API Key

client = OpenAI(base_url=API_URL,
                api_key=API_KEY)
