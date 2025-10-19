import requests
import argparse
import sys

# Replace with your OpenWeatherMap API key
API_KEY = '30.2937, 120.1614'  # Get this from https://openweathermap.org/api
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    """ Fetch weather data for the given city."""
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise error for bad responses
        data = response.json()
        
        # Extract relevant data
        city_name = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        description = data['weather'][0]['description'].capitalize()
        
        # Print formatted output
        print(f"Weather in {city_name}, {country}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Description: {description}")
    
    except requests.exceptions.HTTPError as e:
        if response.status_code == 401:
            print("Error: Invalid API key. Please check your OpenWeatherMap API key.")
        elif response.status_code == 404:
            print(f"Error: City '{city}' not found. Please check the spelling.")
        else:
            print(f"HTTP Error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Network Error: {e}")
    except KeyError:
        print("Error: Unexpected response format from API.")

def main():
    parser = argparse.ArgumentParser(description="Real-Time Weather CLI Tool")
    parser.add_argument('city', help="Name of the city to get weather for (e.g., 'London')")
    args = parser.parse_args()
    
    if not API_KEY or API_KEY == 'YOUR_API_KEY_HERE':
        print("Error: Please set your OpenWeatherMap API key in the script.")
        sys.exit(1)
    
    get_weather(args.city)

if __name__ == "__main__":
    main()
