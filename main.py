import os
import pandas as pd
from pretty_html_table import build_table
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


SENDER_EMAIL = os.environ["SENDER_EMAIL"]
SENDER_PASSWORD = os.environ["SENDER_PASSWORD"]
# Mostly gmail server would be 'smtp.gmail.com:587'
SERVER = os.environ["GMAIL_SERVER"]
RECEIVER_EMAIL = os.environ["RECEIVER_EMAIL"]


SUBJECT = 'Table Email Template'


def get_table_data() -> pd:
    original_data = {'Name': ('name1', 'name2'), 'age': (28, 26)}
    table_data = pd.DataFrame(original_data)
    return table_data


def pretty_table():
    data = get_table_data()
    pretty_data = build_table(data, color='green_light')
    return pretty_data


def _generate_message() -> MIMEMultipart:
    message = MIMEMultipart()
    message['Subject'] = SUBJECT
    message['From'] = SENDER_EMAIL
    message['To'] = RECEIVER_EMAIL
    return message


def send_mail(body):
    message = _generate_message()
    content_body = body
    message.attach(MIMEText(content_body, 'html'))
    server = SMTP(SERVER)
    server.ehlo()
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message.as_string())
    server.quit()


if __name__ == '__main__':
    pretty_table_data = pretty_table()
    send_mail(pretty_table_data)
