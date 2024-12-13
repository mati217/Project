import urllib.request
import json


def address(lat, lon):
  key = 'bdc_a4fdd490b1554e869dd430a821214fd8'
  url = f'https://api-bdc.net/data/reverse-geocode?latitude={lat}&longitude={lon}&localityLanguage=en&key={key}'
  request = urllib.request.urlopen(url)
  result = json.loads(request.read())

  return result
