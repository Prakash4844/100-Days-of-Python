import datetime as dt
from smtplib import SMTP
from email.mime.text import MIMEText
import random
import os

subject = "Thursday Motivation ;)"
sender = "prakashsahu0518@gmail.com"
recipients = ["johnathanjoestar@myyahoo.com"]
password = os.environ.get("SMTP_APP_PASSWORD")


def send_email(email, recipient_emails, app_password):
    with SMTP('smtp.gmail.com', 587) as smtp_server:
        smtp_server.starttls()
        smtp_server.login(email, app_password)
        msg['To'] = ', '.join(recipient_emails)
        smtp_server.sendmail(email, recipient_emails, msg.as_string())

    print(f"Message sent! to {recipient_emails}")


now = dt.datetime.now()
weekday = now.weekday()

if weekday == 4:
    try:
        with open("quotes.txt") as file:
            quotes = file.readlines()
            body = random.choice(quotes)
    except FileNotFoundError:
        print("No quotes file found")
    else:
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        send_email(sender, recipients, password)

else:
    print("Nope, not today!")
