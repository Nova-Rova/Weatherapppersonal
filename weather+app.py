from pyowm import OWM
from dotenv import load_dotenv
from google import genai
from google.genai import types
load_dotenv()
import os
WEATHER_API_KEY = os.getenv("weather_API_KEY")
owm = OWM(WEATHER_API_KEY)
mgr = owm.weather_manager()
observation = mgr.weather_at_place("accra")
weather = observation.weather
wind_speed = weather.wind()["speed"]
wind_direction = weather.wind()["deg"]
temperature = weather.temperature("celsius")["temp"]
temperature_feels_like = weather.temperature("celsius")["feels_like"]
temperature_min = weather.temperature("celsius")["temp_min"]
temperature_max = weather.temperature("celsius")["temp_max"]
humidity = weather.humidity
detailed_status = weather.detailed_status
forcast = mgr.forecast_at_place("accra", "3h")
weather_forcast = forcast.forecast
forcast_weather = weather_forcast.weathers
forcast_wind_speed = forcast_weather[0].wind()["speed"]
forcast_wind_direction = forcast_weather[0].wind()["deg"]
forcast_temperature = forcast_weather[0].temperature("celsius")["temp"]
forcast_temperature_feels_like = forcast_weather[0].temperature("celsius")["feels_like"]
forcast_temperature_min = forcast_weather[0].temperature("celsius")["temp_min"]
forcast_temperature_max = forcast_weather[0].temperature("celsius")["temp_max"]
forcast_humidity = forcast_weather[0].humidity
forcast_detailed_status = forcast_weather[0].detailed_status


client = genai.Client()
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"""
    Give a detailed weather report for Accra, Ghana based on the following data in a very fun and engaging way.:
    Current Weather:
    - Wind Speed: {wind_speed} m/s
    - Wind Direction: {wind_direction} degrees
    - Temperature: {temperature} °C
    - Feels Like: {temperature_feels_like} °C
    - Minimum Temperature: {temperature_min} °C
    - Maximum Temperature: {temperature_max} °C
    - Humidity: {humidity}%
    - Detailed Status: {detailed_status}
    Forecasted Weather (Next 3 Hours):
    - Wind Speed: {forcast_wind_speed} m/s
    - Wind Direction: {forcast_wind_direction} degrees
    - Temperature: {forcast_temperature} °C
    - Feels Like: {forcast_temperature_feels_like} °C
    - Minimum Temperature: {forcast_temperature_min} °C
    - Maximum Temperature: {forcast_temperature_max} °C
    - Humidity: {forcast_humidity}%
    - Detailed Status: {forcast_detailed_status}
""",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0) # Disables thinking
    ),
)
print(response.text)