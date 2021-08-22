from django.conf import settings
from django.shortcuts import render
import requests
import json


def my_view():
    r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=riga&appid={settings.WEATHER_API_KEY}')
    print("My Status Code")
    print(r.status_code)
    return render('template.html', "")

