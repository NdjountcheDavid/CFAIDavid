import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from config import Config

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

def send_email(subject, body):
    """Send an email alert with the news."""
    msg = MIMEText(body)
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
