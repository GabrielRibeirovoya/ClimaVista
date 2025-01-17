import requests
import json
import os
from datetime import date
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')

def kelvin_converter(kelvin, formatting):
    if formatting == 'Celsius':
        formatting = round(kelvin - 273.15, 2)
    elif formatting == 'Fahrenheit':
        formatting = round(kelvin - 459.67, 2)
    else:
        formatting = kelvin

    return formatting

def request_city(city_name, formatting):
    link = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'
    request = requests.get(link)
    data = request.json()

    weather = data['weather'][0]['main']
    description = data['weather'][0]['description']

    temp = data['main']['temp']
    temp = kelvin_converter(temp, formatting)

    temp_min = data['main']['temp_min']
    temp_min = kelvin_converter(temp_min, formatting)

    temp_max = data['main']['temp_max']
    temp_max = kelvin_converter(temp_max, formatting)

    humidity = data['main']['humidity']

    pressure = data['main']['pressure']

    time_today = {'city': city_name, 
                  'weather': weather, 
                  'description': description, 
                  'temp': temp, 
                  'temp_min': temp_min,
                  'temp_max': temp_max,
                  'humidity': humidity,
                  'pressure': pressure
                  }
    
    return time_today

def request_coordinate(lat, lon, formatting):
    link = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}'
    request = requests.get(link)
    data = request.json()

    longitude = data['coord']['lon']
    latitude = data['coord']['lat']

    weather = data['weather'][0]['main']
    description = data['weather'][0]['description']

    temp = data['main']['temp']
    temp = kelvin_converter(temp, formatting)

    temp_min = data['main']['temp_min']
    temp_min = kelvin_converter(temp_min, formatting)

    temp_max = data['main']['temp_max']
    temp_max = kelvin_converter(temp_max, formatting)

    humidity = data['main']['humidity']

    pressure = data['main']['pressure']

    time_today = {'latitude': longitude,
                  'longitude': latitude,
                  'weather': weather, 
                  'description': description, 
                  'temp': temp, 
                  'temp_min': temp_min,
                  'temp_max': temp_max,
                  'humidity': humidity,
                  'pressure': pressure
                  }
    
    return time_today


