from smtplib import *
from email.mime.text import MIMEText
import os

subject = "Testing smtplib module in python"
body = "This is some random Email body text. send by Prakash using Python smtplib module"
sender = "prakashsahu0518@gmail.com"
recipients = ["lomipo4149@niback.com", "mipsigitri@gufum.com"]
password = os.environ.get("SMTP_APP_PASSWORD")
msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = sender


def send_email(email, recipient_emails, app_password):
    with SMTP('smtp.gmail.com') as smtp_server:
        smtp_server.starttls()
        smtp_server.login(email, app_password)
        msg['To'] = ', '.join(recipient_emails)
        smtp_server.sendmail(email, recipient_emails, msg.as_string())

    print(f"Message sent! to {recipient_emails}")


send_email(sender, recipients, password)
