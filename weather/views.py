import requests #type: ignore
from django.shortcuts import render
from django.conf import settings
from decouple import config

API_KEY = settings.OPENWEATHER_API_KEY  

def weather_view(request):
    weather_data = None
    error = None

    if request.method == 'GET' and 'city' in request.GET:
        city = request.GET['city']
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ua'

        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
        else:
            error = 'Місто не знайдено 😞'

    return render(request, 'weather/weather.html', {
        'weather': weather_data,
        'error': error
    })
