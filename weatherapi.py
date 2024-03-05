import requests

def fetch_weather(city):
    api_key = "600379262101b2163447421f32b5c8dc"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

def display_weather(weather_data):
    if weather_data["cod"] == 200:
        print(f"Weather in {weather_data['name']}:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Weather Condition: {weather_data['weather'][0]['description']}")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
        print(f"Humidity: {weather_data['main']['humidity']}%")
    else:
        print(f"Error: {weather_data['message']}")

def main():
    city = input("Enter city name: ")
    weather_data = fetch_weather(city)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
