# 9) Make a list of all dogs that have names of 5 characters or less. Use a for loop.

dogs = ["Sparky", "Jane", "Matilda", "Blartsburg"]
dogs.append("Maxwell")

short_named_dogs = []
for dog in dogs:
  print(dog)
  if len(dog) <= 5:
    print(dog, "has a short name")
    # Add the dog to our list
    short_named_dogs.append(dog)
  else:
    print(dog, "has a long name")
print(short_named_dogs)

short_named_dogs = [dog for dog in dogs if len(dog) <= 5]
print(short_named_dogs)

# 10) I'm on a web page with some links about Zurich, and the URL looks like this: http://important-swiss-things.ch/docs/download/ZH. I want it for all of the following, too.

cantons = [ "ZH", "BE", "LU", "UR", "SZ", "OW", "NW", "GL", "ZG", "FR", "SO", "BS", "BL", "AR", "AI", "SG", "GR", "AG", "TG", "TI", "VD", "VS", "NE", "GE", "JU"]

base = "http://important-swiss-things.ch/docs/download/"
for canton in cantons:
  print(base + canton)

# List comprehension style
new_urls = [base + canton for canton in cantons]
print(new_urls)

# 11) I'm trying to get some top-secret documents from top-secret-secrets.com, and I know the URL pattern but I don't want to type them all out individually! Programmers are lazy, remember?

# Each secret document has a document ID and is 12 pages long, with pages "001.pdf" through "012.pdf". Each page is available at a different URL. For example, for the document ID of QQ7LTHM, the pages are available at

# www.top-secret-pdfs.com/content/secrets/QQ7LTHM/page/001.pdf
# www.top-secret-pdfs.com/content/secrets/QQ7LTHM/page/002.pdf
# www.top-secret-pdfs.com/content/secrets/QQ7LTHM/page/003.pdf

ids = ['qq7lthm','jemsqhg','O6itcke', 'cp4Iua0','bkijcmo','ctoyjrm','z8wc6xy','zk4Bmm0']
pages = ['001', '002', '003', '004', '005', '006', '007', '008', '009', '010', '011', '012']

base = "www.top-secret-pdfs.com/content/secrets/"
for id in ids:
  for page in pages:
    print(base + id.upper() + "/page/" + page + ".pdf")

for id in ids:
  for page in range(1, 13):
    print("{base}{id}/page/{page:03}.pdf".format(base=base, id=id.upper(), page=page))



import csv

csvfile = open('countries.csv', 'r')
reader = csv.DictReader(csvfile)
data = list(reader)
csvfile.close()

countries = data

# 1) What are the columns in our dataset?

# Just look at the first one
print(countries[0])

# We just want the keys
print(countries[0].keys())

# 2) How many countries do we have in our dataset?

print(len(countries))

# 3) How many countries in Asia? How about North America?

count_asia = 0
count_na = 0
for country in countries:
  if country['Continent'] == 'Asia':
    count_asia = count_asia + 1

  if country['Continent'] == 'N. America':
    count_na = count_na + 1

print("There are", count_asia, "countries in Asia")
print("There are", count_na, "countries in North America")

asia_countries = [country for country in countries if country['Continent'] == 'Asia']
print("There are", len(asia_countries), "counries in Asia")

na_countries = [country for country in countries if country['Continent'] == 'N. America']
print("There are", len(na_countries), "counries in North America")

# 4) What is the total population of the world?

# Life would be great if we could just use 'sum'
# in order to use sum, we need a list of all 'Population' columns

populations = [int(country['Population']) for country in countries]
print(populations)
print("Total population of the world is", sum(populations))

# 5) Which has a larger population, Africa or South America?
africa_populations = [int(country['Population']) for country in countries if country['Continent'] == 'Africa']
sa_populations = [int(country['Population']) for country in countries if country['Continent'] == 'S. America']

if sum(africa_populations) > sum(sa_populations):
  print("Africa has a larger population")
else:
  print("South AMerica has a larger population")

# 11) Calculate the 75th percentile of GDP.
import numpy

gdps = [int(country['GDP_per_capita']) for country in countries]

seventy_fifth_percentile = numpy.percentile(gdps, 75, interpolation='midpoint')
print(seventy_fifth_percentile)

# 12) What percent of the world population has a life expectancy of below 50 years? Above 80 years?

below_50_populations = [int(country['Population']) for country in countries if float(country['life_expectancy']) < 50]
total_below_50 = sum(below_50_populations)
total_population = sum(populations)
print(total_below_50 / total_population * 100)


below_80_populations = [int(country['Population']) for country in countries if float(country['life_expectancy']) < 80]
total_below_80 = sum(below_80_populations)
total_population = sum(populations)
print(total_below_80 / total_population * 100)


