import requests

API_KEY = '96e728e7d0fbe4a958a4d7d532831db6'

lat = 28.704060
lon = 77.102493

API_URL = 'https://api.openweathermap.org/data/2.5/onecall'

params = {
    'lat': lat,
    'lon': lon,
    'appid': API_KEY,
}

response = requests.get(API_URL, params=params)


weather_data = response.json()
print(weather_data)