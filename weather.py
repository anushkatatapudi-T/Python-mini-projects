import requests
print("========================")
print("Weather App  is starting")
print("=========================")
n = input("Enter your city name : ")
url = 'https://geocoding-api.open-meteo.com/v1/search'
response = requests.get(url,params={
    'name':n,
    'count':1,
    'language':'en',
    'format':'json'
})
print("Successfully running : ",response.status_code)

data = response.json()
if 'results' in data :
    city = data['results'][0]
    latitude=city['latitude']
    longitude=city['longitude']
    print("City : ",city['name'])
    print("Latitude:",latitude)
    print("Longitude:",longitude)
    weather_url = 'https://api.open-meteo.com/v1/forecast'
    weather_response=requests.get(weather_url,params={
        'latitude':latitude,
        'longitude':longitude,
        'current':
        "temperature_2m,relative_humidity_2m,apparent_temperature,wind_speed_10m,weather_code"
    })
    print(weather_response.status_code)
    data2=weather_response.json()
    if 'current' in data2:
        current=data2['current']
        weather_code = current['weather_code']

        weather_descriptions = {
                0: "Clear sky",
                1: "Mainly clear",
                2: "Partly cloudy",
                3: "Overcast",
                45: "Fog",
                48: "Rime fog",
                51: "Light drizzle",
                53: "Moderate drizzle",
                55: "Dense drizzle",
                61: "Slight rain",
                63: "Moderate rain",
                65: "Heavy rain",
                71: "Slight snow",
                73: "Moderate snow",
                75: "Heavy snow",
                80: "Rain showers",
                81: "Moderate rain showers",
                82: "Heavy rain showers",
                95: "Thunderstorm",
                96: "Thunderstorm with hail",
                99: "Thunderstorm with heavy hail"
    
}

        description = weather_descriptions.get(weather_code, "Unknown condition")
        print("Weather:", description)
        temperature_2m =current['temperature_2m']
        relative_humidity_2m = current['relative_humidity_2m']
        apparent_temperature = current['apparent_temperature']
        wind_speed_10m = current['wind_speed_10m']
        print("\n===== WEATHER REPORT =====")
        print("Temperature:", temperature_2m, "°C")
        print("Humidity:", relative_humidity_2m, "%")
        print("Feels like:", apparent_temperature, "°C")
        print("Wind Speed:", wind_speed_10m, "km/h")
        print("Weather :",description)
    else :
        print("No weather found!")


else:
    print("City not found!")