import requests
import os
clear = lambda: os.system('cls')
            
def getWeatherCity():
    city = input("Enter City Name : ")
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + " &appid=585c10c2fdc788ae2d52fa7bac21c133"
    json_data = requests.get(api).json()
    humidity = json_data['main']['humidity']
    press = json_data['main']['pressure']
    temp = int(json_data['main']['temp']- 273.15)
    speed = json_data['wind']['speed']
    degree = json_data['wind']['deg']

    final_data = "\n" + "Humidity : " +str(humidity) + "\n" + "Pressure : " + str(press) + "\n" +"Temperature : " + str(temp) +"°C" + "\n" + "Wind Speed : " + str (speed) + "\n" + "Wind Degree : " + str(degree)
    
    print(final_data)
getWeatherCity()

