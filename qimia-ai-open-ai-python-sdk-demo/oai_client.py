from openai import OpenAI

API_URL: str = "https://api.qimiaai.com"
API_KEY: str = "your_api_key_here"  # Your valid Qimia AI API Key

client: OpenAI = OpenAI(base_url=API_URL,
                        api_key=API_KEY)
