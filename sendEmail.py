import start 
import os
import smtplib
import email.message
import json
import requests
from dotenv import load_dotenv
input('')
load_dotenv()

key = os.getenv('KEY_EMAIL')
user = os.getenv('USER_EMAIL')

def info():
    data = {}

    current_directory = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_directory, 'sender.json')

    if os.path.exists(file_path):
        with open(file_path, 'r') as arquivo:
            data = json.load(arquivo)
    else:
        print('Arquivo sender.json não encontrado!')

    city = data['city']
    formatting = data['formatting']
    data_time =  start.colectorTime(city, formatting)
    body = f'O tempo na cidade de {city} estará com {data_time['weather']} com a seguinte descrição: {data_time['description']}. A temperatura será em torno de {data_time['temp']}°C, com a mínima chegando a {data_time['temp_min']}°C e a máxima podendo atingir {data_time['temp_max']}°C. A umidade relativa do ar está em {data_time['humidity']}% e a pressão atmosférica é de {data_time['pressure']} hPa.'

    send_email('Clima do Dia', data['email'], body)


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
    print('E-mail enviado!')

info()