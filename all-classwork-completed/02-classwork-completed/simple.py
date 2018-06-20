# Lists

print("Hello world")

name = "Smush"
name2 = "Boy Abby"
name3 = "Stumpy"

print("Hello", name)
print("Hello", name2)
print("Hello", name3)

names = ["Smush", "Boy Abby", "Stumpy", "Luca", "Luna"]
print("Hello", names)

for name in names:
  print("Hello", name)

ages = [8, 14, 9, 1, 2]
print(ages)

print("I have", len(ages), "cats")
print("Their total years are", sum(ages))
print(ages)
print(sorted(ages))
print(ages)

sorted_ages = sorted(ages)
print(sorted_ages)

# ages = sorted(ages)

# ~👻~ FORGET THIS EXISTS ~👻~
# ages.sort()
# print(ages)
# ~👻~ SERIOUSLY ~👻~


print(ages)
print(max(ages))
print(min(ages))

# Give me the first one!
print(names[0])
print(names[1])
print(names[2])

print("The last element of the list is", names[-1])

print(sorted(names))


# print(mean(ages))
print(sum(ages) / len(ages))


import statistics
print(statistics.mean(ages))
print(statistics.median(ages))


import statistics as stats
print(stats.mean(ages))
print(stats.median(ages))

import statistics as potatoes
print(potatoes.mean(ages))
print(potatoes.median(ages))

from statistics import mean
from statistics import median
print(mean(ages))
print(median(ages))

# Dictionaries!
names = ["Smush", "Boy Abby", "Stumpy", "Luca", "Luna"]
ages = [8, 14, 9, 1, 2]







smush_name = "Smush"
smush_age = 8

abby_name = "Boy Abby"
abby_age = 14

# Dictionaries
smush = { "name": "Smush", "age": 8 }
print("Hello", smush)
print(smush['name'])
print(smush['age'])
print(smush.keys())

abby = {
  'name': 'Boy Abby',
  'age': 14
}

# The cat's name is Boy Abby and he is 14 years old
print("the cat's name is", abby['name'], "and he is", abby['age'])

populations = {
  'Los Angeles': 2,
  'Brooklyn': 3,
  'DC': 7
}

print(populations['Brooklyn'])

city = 'DC'
print(populations[city])


cityname = input("What city are you interested in?")

if cityname in populations.keys():
  print("The population is", populations[cityname])
else:
  print("I don't know...")

num = 2
if num in [1, 2, 3, 4]:
  print("the number is inside of the list")



