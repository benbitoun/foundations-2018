# APIs
# Application Programming Interface

# JSON
# JavaScript Object Notation

# https://swapi.co/api/people/1/

# statistics package/module/library
# package/module one for internet stuff???
# library for downloading web pages??

import requests

response = requests.get('https://swapi.co/api/people/2/')

print(response.text)
print(type(response.text))
print(response.json()['url'])

data = response.json()

print(data['url'])


print(data['name'], "has", data['hair_color'], "hair")

for film in data['films']:
  # Endpoints!
  # print(film)

  # Take the URL of the film C3-PO is in,
  # Use requests to download it
  # Turn that JSON response into a dictionary
  # and print out the data
  response = requests.get(film)
  film_data = response.json()
  print(film_data['title'])


# https://api.darksky.net/forecast/15074402c474e3dab67f7377e1f95519/37.8267,-122.4233
# API key = 15074402c474e3dab67f7377e1f95519


response = requests.get('https://api.darksky.net/forecast/15074402c474e3dab67f7377e1f95519/37.8267,-122.4233')
data = response.json()
print(data)

