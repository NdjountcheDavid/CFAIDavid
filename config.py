import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Email settings
    EMAIL_USER = os.getenv("EMAIL_USER")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
    RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")
    MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

    # Websites to scrape
    TARGET_WEBSITES = [
        "https://www.ign.com/news",
        "https://www.gamespot.com/news/"
    ]

    # Keywords to filter news
    KEYWORDS = ["release", "update", "trailer", "review", "announce"]

    # Scraping interval (in hours)
    SCRAPE_INTERVAL = 24
