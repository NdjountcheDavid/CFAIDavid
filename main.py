import schedule
import time
from agent import run_agent
from config import Config

def job():
    print("Running agent...")
    run_agent()

if __name__ == "__main__":
    schedule.every(Config.SCRAPE_INTERVAL).hours.do(job)
    print("Agent started. Press Ctrl+C to exit.")
    while True:
        schedule.run_pending()
        time.sleep(60)
