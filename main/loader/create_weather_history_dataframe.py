from settings import OPENWEATHER_API_KEY
import requests
import datetime
import time

API_CALL_LITERAL = "http://api.openweathermap.org/data/2.5/onecall/timemachine?lat=60.99&lon=30.9&dt={}&appid={}"



def create_single_day_dataframe():
    response = requests.get(API_CALL_LITERAL.format(str(round(time.time())), OPENWEATHER_API_KEY))
    print(response.json())
    pass
