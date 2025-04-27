# weather_data.py
import requests

def get_weather(city, api_key):
    base_url = "http://api.weatherapi.com/v1/current.json?"
    complete_url = f"{base_url}key={api_key}&q={city}"
    response = requests.get(complete_url)
    data = response.json()

    if 'error' not in data:
        current_weather = data['current']
        temperature = current_weather['temp_c']
        pressure = current_weather['pressure_mb']
        humidity = current_weather['humidity']
        description = current_weather['condition']['text']

        weather_data = {
            "city": city,
            "temperature": temperature,
            "pressure": pressure,
            "humidity": humidity,
            "description": description
        }
        return weather_data
    else:
        return None
