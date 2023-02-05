import os
from dotenv import load_dotenv
import requests

def getweather(title):
  # this will load variables from .env.
  load_dotenv() 
  # Current Weather API Endpoint Params
  params = {
    'access_key': os.getenv("API-KEY"),
    'query': title,
    'units':'f'
  }
  #Call to API endpoint
  api_result = requests.get('http://api.weatherstack.com/current', params)
  #Getting response
  api_response = api_result.json()
  #Loading data
  city = api_response['location']['name']
  tempurature = api_response['current']['temperature']
  forcast  = api_response['current']['weather_descriptions'][0]
  humidity = api_response['current']['humidity']
  feelsLike = api_response['current']['feelslike']
  time = api_response['current']['observation_time']
  #Formatting Data
  data = f'City: {city} , Observed time: Today at {time} , Temp: {tempurature} F , Forcast: {forcast} , Humidity: {humidity} , FeelsLike: {feelsLike} F'
  #Sending Data Back to endpint
  return data