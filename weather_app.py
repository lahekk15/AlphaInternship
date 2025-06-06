import requests


key = "4df87db421d5b0c99108a61f60ad4866"

city = input("Enter city name: ")

url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    'q': city,
    'appid': key,
    'units': 'metric'  
}

response = requests.get(url, params=params)

if response.status_code == 200:

    data = response.json()
    weather_desc = data['weather'][0]['description']
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    print(f"Weather in {city.title()}:")
    print(f"Description: {weather_desc}")
    print(f"Temperature: {temp}°C")
    print(f"Feels like: {feels_like}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind speed: {wind_speed} m/s")
else:

    print(f"Couldn't retrieve data for '{city}'.")
