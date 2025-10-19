# Real-Time Weather CLI Tool

A simple, lightweight command-line interface (CLI) tool built in Python that fetches and displays real-time weather data for any city using the OpenWeatherMap API. It provides key details such as temperature, humidity, wind speed, and weather description. Perfect for quick weather checks from the terminal.

## Features
- Fetches real-time weather data for user-specified cities.
- Displays temperature (in Celsius or Fahrenheit), humidity, wind speed, and weather description.
- Handles errors gracefully (e.g., invalid city, API key issues, network problems).
- Easy to use with command-line arguments.
- Customizable units (metric or imperial).
- Minimal dependencies for quick setup.

## Requirements
- **Python**: Version 3.6 or higher.
- **API Key**: Free account from [OpenWeatherMap](https://openweathermap.org/api) (no credit card required).
- **Libraries**:
  - `requests`: Install via `pip install requests`.
  - `argparse`: Built-in with Python (no installation needed).

## Features
- Fetches real-time weather data for user-specified cities.
- Displays temperature (in Celsius or Fahrenheit), humidity, wind speed, and weather description.
- Handles errors gracefully (e.g., invalid city, API key issues, network problems).
- Easy to use with command-line arguments.
- Customizable units (metric or imperial).
- Minimal dependencies for quick setup.

## Requirements
- **Python**: Version 3.6 or higher.
- **API Key**: Free account from [OpenWeatherMap](https://openweathermap.org/api) (no credit card required).
- **Libraries**:
  - `requests`: Install via `pip install requests`.
  - `argparse`: Built-in with Python (no installation needed).

## Installation
1. Clone or download the repository:
   ```
   git clone https://github.com/nabinkandel07/real-time-weather-cli.git
   cd real-time-weather-cli
   ```
2. Install dependencies:
   ```
   pip install requests
   ```
3. Obtain an API key from [OpenWeatherMap](https://openweathermap.org/api) and replace `'YOUR_API_KEY_HERE'` in `weather_cli.py` with your key.

## Usage
Run the script from the command line with a city name as an argument:
```
python weather.py "City Name"
```
- Example: `python weather.py London`
- Output:
  ```
  Weather in London, GB:
  Temperature: 15.5°C
  Humidity: 72%
  Wind Speed: 3.5 m/s
  Description: Broken clouds
  ```

## Configuration
- **Units**: By default, temperature is in Celsius. To switch to Fahrenheit, change 'units': 'metric' to 'units': 'imperial' in the `get_weather` function.
- **API Key**: Ensure your key is set in the script. For security, consider using environment variables (e.g., via `os.environ`) instead of hardcoding.

## Examples
- Query a city: `python weather.py "New York"`
- Handle errors: If the city is not found, you'll see: `Error: City 'InvalidCity' not found. Please check the spelling.`
- Invalid API key: `Error: Invalid API key. Please check your OpenWeatherMap API key.`

## Contributing
- Fork the repository and submit a pull request for improvements.
- Report issues or suggest features via GitHub Issues.


## Notes
- **Rate Limits**: The free OpenWeatherMap tier allows up to 60 calls per minute. Upgrade for higher limits if needed.
- **Extensions**: Easily expandable to include weather forecasts by modifying the API endpoint to `/forecast`.
- **Testing**: Test with various cities and ensure your API key is active. If you encounter issues, check your internet connection or API key validity.
```
