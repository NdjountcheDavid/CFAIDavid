from tools import fetch_video_game_news, send_email, filter_news
from memory import load_memory, add_to_memory
from config import Config

def run_agent():
    """Run the news agent."""
    memory = load_memory()
    new_news = []

    for url in Config.TARGET_WEBSITES:
        news_items = fetch_video_game_news(url)
        filtered_items = filter_news(news_items)
        for item in filtered_items:
            if item not in memory:
                new_news.append(item)

    if new_news:
        email_body = "\n".join([f"{headline}: {link}" for headline, link in new_news])
        send_email("New Video Game News!", email_body)
        add_to_memory(new_news, memory)
        print(f"Sent {len(new_news)} news items.")
    else:
        print("No new news.")
