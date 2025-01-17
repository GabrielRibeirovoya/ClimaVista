import os
import smtplib
import email.message

from dotenv import load_dotenv

load_dotenv()

key = os.getenv('KEY_EMAIL')
user = os.getenv('USER_EMAIL')

def send_email(subject, from_user, email_body):
    msg = email.message.Message()
    msg['Subject'] = subject
    msg['From'] = user
    msg['to'] = from_user
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_body)

    send = smtplib.SMTP('smtp.gmail.com: 587')
    send.starttls()
    send.login(msg['From'], key)
    send.sendmail(msg['From'], msg['to'], msg.as_string().encode('utf-8'))