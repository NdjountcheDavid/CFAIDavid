from tools import fetch_video_game_news, send_email
from memory import load_memory, add_to_memory
from config import Config

def run_agent():
    memory = load_memory()
    new_news = []

    for url in Config.TARGET_WEBSITES:
        news_items = fetch_video_game_news(url)
        for item in news_items:
            if item not in memory:
                new_news.append(item)

    if new_news:
        send_email("New Video Game News!", new_news)
        add_to_memory(new_news, memory)
        print(f"Sent {len(new_news)} news items.")
    else:
        print("No new news.")
