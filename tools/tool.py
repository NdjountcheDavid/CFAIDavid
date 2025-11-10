from llm_tools import summarize_news, classify_news
from config import Config
import smtplib
from email.mime.text import MIMEText
import requests
from bs4 import BeautifulSoup


def fetch_video_game_news(url):
    """Fetch and parse video game news from a given URL."""
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Adjust selectors based on the website structure
        headlines = [h.text.strip() for h in soup.select('h3, h2')]
        links = [a['href'] for a in soup.select('a') if 'href' in a.attrs]
        return list(zip(headlines, links))
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return []


def send_email(subject, news_items):
    """Send an email with summarized news."""
    summaries = []
    for headline, link in news_items:
        summary = summarize_news(headline)
        category = classify_news(headline)
        summaries.append(f"{category.upper()}: {summary} ([Read more]({link}))")

    email_body = "\n\n".join(summaries)
    msg = MIMEText(email_body)
    msg['Subject'] = subject
    msg['From'] = Config.EMAIL_USER
    msg['To'] = Config.RECIPIENT_EMAIL

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(Config.EMAIL_USER, Config.EMAIL_PASSWORD)
        server.send_message(msg)


def filter_news(news_items):
    """Filter news based on keywords."""
    filtered = []
    for headline, link in news_items:
        if any(keyword in headline.lower() for keyword in Config.KEYWORDS):
            filtered.append((headline, link))
    return filtered