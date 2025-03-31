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

def fetch_covid_info(city):
    url = 
    response = requests.get(url)

