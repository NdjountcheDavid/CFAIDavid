# Video Game News Agent

An AI agent that scrapes video game news and sends email alerts.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt

2. run the script:
```bash
python main.py


---

### **How to Use**
1. Install dependencies: `pip install -r requirements.txt`.
2. Set up `.env` with your email credentials.
3. Run the agent: `python main.py`.

### **Notes**
- Adjust `fetch_video_game_news` selectors for each target website.
- For RSS feeds, use the `feedparser` library instead of `requests` + `BeautifulSoup`.
- Test the agent locally before deploying to a server.
