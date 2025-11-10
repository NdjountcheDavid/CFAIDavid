from mistralai.client import MistralClient
from config import Config

client = MistralClient(api_key=Config.MISTRAL_API_KEY)

def summarize_news(news_text):
    """Summarize news using Mistral LLM."""
    response = client.chat(
        model="mistral-tiny",
        messages=[
            {"role": "user", "content": f"Summarize this video game news in one sentence: {news_text}"}
        ]
    )
    return response.choices[0].message.content

def classify_news(news_text):
    """Classify news (e.g., 'release', 'update', 'review')."""
    response = client.chat(
        model="mistral-tiny",
        messages=[
            {"role": "user", "content": f"Classify this video game news into one of these categories: release, update, review, trailer, other. News: {news_text}"}
        ]
    )
    return response.choices[0].message.content
