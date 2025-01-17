import requests
import json
from key import API_KEY
from datetime import date
from translate import Translator

city_name = 'São Paulo'
API_KEY = 'a4ee089af1ce062e2040bd31f6a2633f'
link = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'
request = requests.get(link)

data = request.json()

description = data['weather'][0]['description']

translator= Translator(to_lang="pt")
desc = translator.translate(str(description))

print(f'Em {city_name} - {date.today()}, o clima esta com {description}.')