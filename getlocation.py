import json
import urllib.request


def get_location():
  url = "http://api.open-notify.org/iss-now.json"
  response = urllib.request.urlopen(url)

  obj = json.loads(response.read())
  long = obj['iss_position']['longitude']
  lat = obj['iss_position']['latitude']
  return lat, long
