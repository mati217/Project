from flask import Flask, render_template

from getlocation import get_location

from getweather import get_weather
from getdistance import dist
from getreversegeo import address
from getcountry import country

app = Flask('app')


@app.route('/')
def ind():
  #Location of ISS
  loc = get_location()
  lat, long = loc[0], loc[1]
  print(lat)
  print(long)
  #Weather
  weather = get_weather(lat, long)

  temp_c = round(weather["main"]["temp"] - 273.15, 2)
  description = weather["weather"][0]["description"]

  #reverse geolocation
  add = address(lat, long)

  if (add["countryCode"] == ""):
    message = "No Country. The ISS is over water."

    flag = "None"

  else:

    location = add["countryCode"]
    # print(add["countryCode"])
    flag = country(location)[0]["flags"]["png"]
    message = "Country is " + country(location)[0]["name"]["common"]

  #the distance between ISS and myself in Sudbury
  distance = dist(lat, long, 46.5234124, -80.9474222)
  #pass the google map location
  googlemap = f'https://www.google.com/maps/place/{lat}+{long}'

  return render_template("index.html",
                         long=long,
                         lat=lat,
                         temp=temp_c,
                         desc=description,
                         distance=distance,
                         message=message,
                         googlemap=googlemap,
                         flag=flag)


app.run(host='0.0.0.0', port=8080)
