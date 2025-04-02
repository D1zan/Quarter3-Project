import requests 
import json

#creating the class 
class Weather:
    def __innit__(self, city, visibility):
        self.city = city
        self.visibility = visibility 

    def display_info(self):
        print(f"City: {self.city}")
        print(f"Visibility: {self.visibility}") 
#Getting the API

def fetch_info(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid=b8712e4fd9e37511cf9f72ef17c1c6dc"
    response = requests.get(url)
    
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print(f"\n This information is not available to you\n")
#Albania, Tirana (41, 20)
#SwiTzerland, Bern (47, 8)
#Japan,Tokyo (35.67,139.65)
#United States, Washington DC (38, -97)
#Zocca, Rome (42.83, 12.83)

def info(weather_json):
    weather = Weather(
        weather_json["city"],
        weather_json["visibility"]
    )
    return weather()

#User input 

print("Hey, Welcome to Weather App: \nIn this program you will choose a location from the given list, \nand the program will give you interesting weather information")
#Loop

while True:
    print("These are the ones available: \n")
    print("Tirana, Albania,\nBern, Switzerland,\nTokyo, Japan,\nWashington DC, United States,\nRome, Italy.")
    cities = input("Which location would you like to choose?: ").lower().strip()
    temp_info = fetch_info()

    if not info: 
        continue