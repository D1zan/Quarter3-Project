import requests 
import json

#creating the class 
class weather:
    def __innit__(self, city, temperature):
        self.city = city
        self.temperature = temperature 

    def display_info(self):
        print(f"City: {self.city}")
        print(f"Temperature: {self.temperature}") 
#Getting the API

def fetch_info(lat, lon):
    url = f"https://pro.openweathermap.org/data/2.5/forecast/hourly?lat={lat}&lon={lon}&appid=b8712e4fd9e37511cf9f72ef17c1c6dc"
    response = requests.get(url)
    return response

print(fetch_info(35.67619190, 139.65031060))