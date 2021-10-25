import requests
import time
import os
clear = lambda: os.system('cls')

def main():
    clear()
    print("WEATHER FORECAST APPLICATION")
    option = input("""
    1.Search By City Name
    2.Search By Location ( lat / long )
    3.Search By Date
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
    elif userChoice == '3':
        getWeatherDate()
      
            
def getWeatherCity():
    city = input("Enter City Name : ")
    # api = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude={part}&appid=605c2f5435c095f8d06858739fe0d87b".format()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=585c10c2fdc788ae2d52fa7bac21c133"
    json_data = requests.get(api).json()
    humidity = json_data['main']['humidity']
    press = json_data['main']['pressure']
    temp = int(json_data['main']['temp']- 273.15)
    speed = json_data['wind']['speed']
    degree = json_data['wind']['deg']

    final_data = "\n" + "Humidity : " +str(humidity) + "\n" + "Pressure : " + str(press) + "\n" +"Temperature : " + str(temp) +"°C" + "\n" + "Wind Speed : " + str (speed) + "\n" + "Wind Degree : " + str(degree)
    
    print(final_data)

def getWeatherLat():
    pass    

def getWeatherDate():
    pass
    
main()

