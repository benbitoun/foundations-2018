# Homework 2, Part 2
# ANSWER KEY

print("=== LIST QUESTIONS ===")

# 1) Make a list called "countries" - it should contain seven different countries and NOT be in alphabetical order

countries = ["Ghana", "Peru", "Austria", "Korea", "Australia", "Mexico", "Italy"]

# 2) Using a for loop, print each element of the list
for country in countries:
  print(country)

# 3) Sort the list permanently.
# There are two ways to do this! They work the same.

# Version 1: Use a function and save it back into the countries variable
countries = sorted(countries)

# Version 2: Use a method that permanently sorts the variable
countries.sort()

for country in countries:
  print(country)

# 4) Display the first element of the list.
print(countries[0])

# 5) Display the second-to-last element of the list.
# Negatives start from the end of the list
print(countries[-2])

# 6) Delete one of the countries from the list using its name.
print("BEFORE:", countries)
countries.remove("Australia")
print("AFTER:", countries)

# 7) Using a for loop, print each country's name in all caps.
for country in countries:
  print(country.upper())

print("=== DICTIONARY QUESTIONS ===")



# These will require LATITUDE and LONGITUDE. You can ask Google for latitude and longitude by typing in *coordinates of CITYNAME*. You can also use http://itouchmap.com/latlong.html. Store the latitude and longitude without the N/S/E/W - if the latitude is S, make it negative. If the longitude is W, make it negative. See here for explanation: https://answers.yahoo.com/question/index?qid=20080211182008AAMdUe8

# 1) Make a dictionary called 'tree' that responds to 'name', 'species', 'age', 'location_name', 'latitude' and 'longitude'. Pick a tree from: https://en.wikipedia.org/wiki/List_of_trees

tree = {
  'species': 'Chinkapin Oak ',
  'name': 'Sacred Oak',
  'age': 500,
  'location_name': 'Oley Valley, Pennsylvania, US',
  'latitude': 40.336,
  'longitude': -75.927
}

# 2) Print the sentence "{name} is a {years} year old tree that is in {location_name}"

# Version 1
print(tree['name'], "is a", tree['age'], "year old tree that is in", tree['location_name'])

# Version 2
sentence = "{} is a {} year old tree that is in {}".format(tree['name'], tree['age'], tree['location_name'])
print(sentence)

# Version 3
sentence = "{name} is a {age} year old tree that is in {location_name}".format(name=tree['name'], age=tree['age'], location_name=tree['location_name'])
print(sentence)

# Version 4
sentence = "{name} is a {age} year old tree that is in {location_name}".format(**tree)
print(sentence)

# 3) The coordinates of New York City are 40.7128° N, 74.0059° W. Check to see if the tree is south of NYC, and print "The tree {name} in {location} is south of NYC" if it is. If it isn't, print "The tree {name} in {location} is north of NYC"

nyc_latitude = 40.7128
if tree['latitude'] < nyc_latitude:
  print("The tree {name} in {location_name} is south of NYC".format(**tree))
else:
  print("The tree {name} in {location_name} is north of NYC".format(**tree))

# 4) Ask the user how old they are. If they are older than the tree, display "you are {XXX} years older than {name}." If they are younger than the tree, display "{name} was {XXX} years old when you were born."

# age = input("How old are you? ")
age = "35" # Fake input
age = int(age)

# You can build these sentences any of the ways above,
# just pick what's most understandable
# Why do I not store age - tree['age'] in a variable?
# ...no good reason, just didn't seem worth it
if age > tree['age']:
  print("You are", age - tree['age'], "years older than", tree['name'])
else:
  print(tree['name'], "was", tree['age'] - age, "years old when you were born")


print("=== LIST OF DICTIONARIES ===")

# 1) Make a list of dictionaries of five places across the world - (1) Moscow, (2) Tehran, (3) Falkland Islands, (4) Seoul, and (5) Santiago. Each dictionary should include each city's name and latitude/longitude (see note above).

places = [{
  'name': 'Moscow',
  'latitude': 55.7558,
  'longitude': 37.6173
}, {
  'name': 'Tehran',
  'latitude': 35.6892,
  'longitude': 51.3890
}, {
  'name': 'Falkland Islands',
  'latitude': -51.7963,
  'longitude': -59.5236
}, {
  'name': 'Seoul',
  'latitude': 37.5665,
  'longitude': 126.9780
}, {
  'name': 'Santiago',
  'latitude': -33.4489,
  'longitude': -70.6693
}]

# 2) Loop through the list, printing each city's name and whether it is above or below the equator (How do you know? Think hard about the latitude.). When you get to the Falkland Islands, also display the message "The Falkland Islands are a biogeographical part of the mild Antarctic zone," which is a sentence I stole from Wikipedia.

for place in places:
  if place['latitude'] > 0:
    print(place['name'], "is above the equator")
  elif place['latitude'] < 0:
    print(place['name'], "is below the equator")
  else:
    print(place['name'], "is on the equator")
  if place['name'] == 'Falkland Islands':
    print("The Falkland Islands are a biogeographical part of the mild Antarctic zone")

# 3) Loop through the list, printing whether each city is north of south of your tree from the previous section.

tree = {
  'species': 'Chinkapin Oak',
  'name': 'Sacred Oak',
  'age': 500,
  'location_name': 'Oley Valley, Pennsylvania, US',
  'latitude': 40.336,
  'longitude': -75.927
}

for place in places:
  if place['latitude'] > tree['latitude']:
    print(place['name'], "is north of", tree['name'])
  elif place['latitude'] < tree['latitude']:
    print(place['name'], "is south of", tree['name'])
  else:
    print(place['name'], "is at the same latitude as", tree['name'])
