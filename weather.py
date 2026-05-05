import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        current = data["current_condition"][0]
        
        temp_f = current["temp_F"]
        feels_like = current["FeelsLikeF"]
        description = current["weatherDesc"][0]["value"]
        humidity = current["humidity"]
        wind_speed = current["windspeedMiles"]
        
        print(f"\n--- Weather for {city} ---")
        print(f"Temperature:  {temp_f}°F")
        print(f"Feels like:   {feels_like}°F")
        print(f"Condition:    {description}")
        print(f"Humidity:     {humidity}%")
        print(f"Wind speed:   {wind_speed} mph")
    else:
        print(f"Could not get weather for {city}. Status code: {response.status_code}")
        
def run_app():
    searched_cities = []
    print("=== Weather App ===")
    while True:
        city = input("\nEnter a city (or 'quit' to exit): ")
        if city.lower() == "quit":
            print("\nCities you searched:")
            for c in searched_cities:
                print(f" - {c}")
            print("Goodbye!")
            break
        get_weather(city)
        searched_cities.append(city)

        again = input("\nSearch another city? (yes/no):")
        if again.lower() == "no":
            print("\nCities you searched:")
            for c in searched_cities:
                print(f" - {c}")
            print("Goodbye!")
            break



run_app()