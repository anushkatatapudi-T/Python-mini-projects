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
print(response.status_code)

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
        "temperature_2m,relative_humidity_2m,apparent_temperature,wind_speed_10m"
    })
    print(weather_response.status_code)
    data2=weather_response.json()
    if 'current' in data2:
        current=data2['current']
        temperature_2m =current['temperature_2m']
        relative_humidity_2m = current['relative_humidity_2m']
        apperent_temperature = current['apparent_temperature']
        wind_speed_10m = current['wind_speed_10m']
        print("\n===== WEATHER REPORT =====")
        print("Temperature:", temperature_2m, "°C")
        print("Humidity:", relative_humidity_2m, "%")
        print("Feels like:", apperent_temperature, "°C")
        print("Wind Speed:", wind_speed_10m, "km/h")
    else :
        print("No weather found!")


else:
    print("City not found!")