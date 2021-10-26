import requests
import time
import os
clear = lambda: os.system('cls')

res = requests.get('https://ipinfo.io/') 
data = res.json()   

def main():
    clear()
    print("WEATHER FORECAST APPLICATION")
    option = input("""
    1.Search By City Name
    2.Search By Location ( lat / long )
                """)
    print(option)

    while True:
        print()
        userChoice = input("Choose An Option: ")
        if userChoice in ['1', '2']:
            break
    if userChoice == '1':
        getWeatherCity()
    elif userChoice == '2':
        getWeatherLat()
            
def getWeatherCity():
    city = input("Enter City Name : ")
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=585c10c2fdc788ae2d52fa7bac21c133"
    json_data = requests.get(api).json()
    humidity = json_data['main']['humidity']
    press = json_data['main']['pressure']
    temp = int(json_data['main']['temp']- 273.15)
    speed = json_data['wind']['speed']
    degree = json_data['wind']['deg']

    final_data = "\n" + "Humidity : " +str(humidity) + "\n" + "Pressure : " + str(press) + "\n" +"Temperature : " + str(temp) +"°C" + "\n" + "Wind Speed : " + str (speed) + "\n" + "Wind Degree : " + str(degree)
    
    print(final_data)
        
getWeatherCity()

def getWeatherLat():
    print("Logged In")
getWeatherLat()
    
main()

