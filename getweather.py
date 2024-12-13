import json
import urllib.request


def get_weather(lat, lon):
  key = "23328991b6856d4ddfe5c34faa25805f"
  url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}'
  request = urllib.request.urlopen(url)
  result = json.loads(request.read())
  return result
