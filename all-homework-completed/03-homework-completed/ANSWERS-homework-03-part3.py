import csv

csvfile = open('countries.csv', 'r')
reader = csv.DictReader(csvfile)
data = list(reader)
csvfile.close()
print("The data looks like", data)

# Answer the following questions based on my favorite boring dataset, countries.csv.

# 1) What are the columns in our dataset?
# Grab the first row, print out the keys
print(data[0].keys())

# 2) How many countries do we have in our dataset?
# 1 row = 1 country, so just see how many rows we have
print(len(data))

# 3) How many countries in Asia? How about North America?

# I'm going to rename the 'data' variable because it's annoying
# that 'data' doesn't actually mean anything

countries = data

# VERSION ONE: for loop and counters
asia_count = 0
na_count = 0
for country in countries:
  if country['Continent'] == 'Asia':
    asia_count = asia_count + 1
  elif country['Continent'] == 'N. America':
    na_count = na_count + 1

print("There are", asia_count, "countries in Asia")
print("There are", na_count, "countries in North America")

# VERSION TWO: list comprehension
# Create new lists, one for Asian countries and one for NA, then use len
asia_countries = [country for country in countries if country['Continent'] == 'Asia']
na_countries = [country for country in countries if country['Continent'] == 'N. America']

print("There are", len(asia_countries), "countries in Asia") 
print("There are", len(na_countries), "countries in North America")

# 4) What is the total population of the world?
# Need to use int(country['Population']) because it thinks it's a string

# VERSION ONE: for loop and a total variable
total = 0
for country in countries:
  total = total + int(country['Population'])
print("The population of the world is", total)

# VERSION TWO: List comprehension to pull out the populations,
# then use sum on it
populations = [int(country['Population']) for country in countries]
print("The total population is", sum(populations))

# 5) Which has a larger population, Africa or South America?

# VERSION ONE: for loop and 2 total variables

africa_total = 0
sa_total = 0
for country in countries:
  if country['Continent'] == 'Africa':
    africa_total = africa_total + int(country['Population'])
  elif country['Continent'] == 'S. America':
    sa_total = sa_total + int(country['Population'])

if africa_total > sa_total:
  print("Africa has more")
else:
  print("South America has more")

# VERSION TWO: list comprehension
# we filter for only africa or only s. america
# and only take the population

african_populations = [int(country['Population']) for country in countries if country['Continent'] == 'Africa']
sa_populations = [int(country['Population']) for country in countries if country['Continent'] == 'S. America']

african_total = sum(african_populations)
sa_total = sum(sa_populations)

if african_total > sa_total:
  print("Africa has more")
else:
  print("South America has more")

# 6) Calculate the total GDP of each country and print it out (right now it's per capita).
# If you don't use int() your life sucks and maybe terminal crashes

for country in countries:
  total_gdp = int(country['Population']) * int(country['GDP_per_capita'])
  print(country['Country'], "-", total_gdp )

# 7) What is the median life expectancy of the world?

import statistics

# VERSION ONE: Create a new list of numbers, use median on it
# Have to use float() instead of int() because decimals

life_expectancies = []
for country in countries:
  life_expectancies.append(float(country['life_expectancy']))

print("Median life expectancy is", statistics.median(life_expectancies))

# VERSION TWO: Use a list comprehension to pull out the life expectancies

life_expectancies = [float(country['life_expectancy']) for country in countries]
print("Median life expectancy is", statistics.median(life_expectancies))

# 8) What is the median life expectancy of Europe?

# VERSION ONE: Create a new list of numbers, use median on it
# Have to use float() instead of int() because decimals

life_expectancies = []
for country in countries:
  if country['Continent'] == 'Europe':
    life_expectancies.append(float(country['life_expectancy']))

print("Median life expectancy in Europe is", statistics.median(life_expectancies))

# VERSION TWO: Use a list comprehension to pull out the life expectancies

life_expectancies = [float(country['life_expectancy']) for country in countries if country['Continent'] == 'Europe']
print("Median life expectancy in Europe is", statistics.median(life_expectancies))

# 9) Print out each country that has a below-average life expectancy.

# VERSION ONE: for loop
life_expectancies = [float(country['life_expectancy']) for country in countries]
median_life_expectancy = statistics.median(life_expectancies)

print("Below average life expectancy:")
for country in countries:
  if float(country['life_expectancy']) < median_life_expectancy:
    print(" -", country['Country'])

# VERSION TWO: list comprehension to filter
life_expectancies = [float(country['life_expectancy']) for country in countries]
median_life_expectancy = statistics.median(life_expectancies)

below_average = [country for country in countries if float(country['life_expectancy']) < median_life_expectancy]

print("Below average life expectancy:")
for country in below_average:
  print(" -", country['Country'])

# 10) Print out each country that has a below-average GDP but an above-average life expectancy.

print("Below average GDP but above-average life expectancy:")

life_expectancies = [float(country['life_expectancy']) for country in countries]
median_life_expectancy = statistics.median(life_expectancies)

gdps = [int(country['GDP_per_capita']) for country in countries]
median_gdp = statistics.median(gdps)

print("Below-average GDP but above-average life expectancy:")
for country in countries:
  if int(country['GDP_per_capita']) < median_gdp and float(country['life_expectancy']) > median_life_expectancy:
    print(" -", country['Country'])


# 11) Calculate the 75th percentile of GDP.

# VERSION ONE: get the 50th percentile, then filter for above-average
# then get the 50th percentile of that
# I'm using list comprehensions because I'm lazy, hopefully you either
# know how they work by now, can translate them into for loops, or also
# don't care

gdps = [int(country['GDP_per_capita']) for country in countries]
median_gdp = statistics.median(gdps)

print("Median GDP is", median_gdp)
above_average_gdps = [gdp for gdp in gdps if gdp > median_gdp]
top_75_gdp = statistics.median(above_average_gdps)
print("75th percentile GDP is", top_75_gdp)

# VERSION TWO: cheat and use numpy
# I've commented it out in case you don't have numpy installed
# import numpy
# top_75_gdp = numpy.percentile(gdps, 75, interpolation='midpoint')
# print("75th percentile GDP is ", top_75_gdp)

# 12) What percent of the world population has a life expectancy of below 50 years? Above 80 years?

# VERSION ONE: for loop
# Keep a running tally of different population counts
below_50_population = 0
above_80_population = 0
total_population = 0

for country in countries:
  # Always increase total_population, but only increase
  # the other two when you need to
  total_population = total_population + int(country['Population'])
  if float(country['life_expectancy']) < 50:
    below_50_population = below_50_population + int(country['Population'])
  if float(country['life_expectancy']) > 80:
    above_80_population = above_80_population + int(country['Population'])

# Do your calculations and print the result
below_50_pct = round(below_50_population / total_population * 100, 2)
above_80_pct = round(above_80_population / total_population * 100, 2)

print("{}% of the world has a life expectancy below 50".format(below_50_pct))
print("{}% of the world has a life expectancy above 80".format(above_80_pct))

# VERSION ONE: list comprehensions
# Make lists of
# 1) All populations
# 2) All populations for < 50 life expectancy
# 3) All populations for > 80 life expectancy
# then use sum() to total them up. Divide by total pop and you have your answer!
all_populations = [int(country['Population']) for country in countries]
total_population = sum(all_populations)

below_50_populations = [int(country['Population']) for country in countries if float(country['life_expectancy']) < 50]
below_50_pct = sum(below_50_populations) / total_population * 100

above_80_populations = [int(country['Population']) for country in countries if float(country['life_expectancy']) > 80]
above_80_pct = sum(above_80_populations) / total_population * 100

# Use .2f to format with two digits after the decimal
print("{:.2f}% of the world has a life expectancy below 50".format(below_50_pct))
print("{:.2f}% of the world has a life expectancy above 80".format(above_80_pct))

