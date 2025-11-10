from llm_tools import summarize_news, classify_news

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
