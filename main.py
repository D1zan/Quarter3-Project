import requests
import json

def fetch_info(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid=b8712e4fd9e37511cf9f72ef17c1c6dc"
    response = requests.get(url)

    if response.status_code == 200:
        return json.loads(response.content)
       
    else:
        print("Error fetching weather data. Check you API for the 1000th time")
        return None

locations = {
    "tirana": (41, 20),
    "bern": (47, 8),
    "tokyo": (35.67, 139.65),
    "washington DC": (38, -97),
    "rome": (42.83, 12.83)
}

# User input
print("\nWelcome to the Weather App!")
print("Choose a location from the list below to get cool weather facts:\n")

# Main Loop
while True:
    for city in locations.keys():
        print(city.title()) #method in python is used to capitalize the first letter of the word 

    user_choice = input("\nWhich location would you like to choose?: ").lower().strip()

    if user_choice in locations:
        lat, lon = locations[user_choice]
        weather_data = fetch_info(lat, lon)

        if weather_data:
            forecast = weather_data["list"][0]  #grabbin the info from inside the dictionaries in the API
            humidity = forecast["main"]["humidity"] #Humidity is inside main
            temperature = forecast["main"]["temp"] #temp is inside main


            print(f"\nWeather in: {user_choice}") 
            print(f"- Temperature: {temperature - 273}°C")
            print(f"- Humidity: {humidity}%")
    keep_going = input("Would you like to ask about another country? (y/n):  ").lower().strip()
    if keep_going == "n":
        break  # Exit the loop 