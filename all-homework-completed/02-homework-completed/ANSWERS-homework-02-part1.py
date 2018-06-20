# Homework 2, Part 1
# ANSWER KEY

print("== LISTS ==")

# 1) Make a list of the following numbers: 22, 90, 0, -10, 3, 22, and 48

numbers = [22, 90, 0, -10, 3, 22, 48]

# 2) Display the number of elements in the list.
print(len(numbers))

# 3) Display the 4th element of this list.
# Remember, 4th element = 3rd index!
print(numbers[3])

# 4) Display the sum of the 2nd and 4th element of the list.
print(numbers[1] + numbers[3])

# 5) Display the 2nd-largest value in the list.

# You need to sort them, then pull the second from the last
sorted_numbers = sorted(numbers)
print("The sorted list is...", sorted_numbers)
print("So the second largest is...", sorted_numbers[-2])

# You could also do this, but I don't think it's readable
print("The second largest is also...", sorted(numbers)[-2])

# 6) Display the last element of the original unsorted list

# We had to use sorted(numbers) instead of numbers.sort() for
# the last one because we still need to use the original list!

print("The last number in the original list is", numbers[-1])

# 7) Display the sum of all of the numbers divided by two.
# sum is part of the standard library, so we don't need to import anything
print(sum(numbers) / 2)

# Print whether the median or the mean of the numbers is higher
# mean and median need the statistics library
import statistics

mean = statistics.mean(numbers)
median = statistics.median(numbers)

if mean > median:
  print("The mean is higher")
elif median > mean:
  print("The median is higher")
else:
  print("The mean and median are equal")

# PART ONE: Dictionaries
print("== DICTIONARIES ==")
# 1) Sometimes dictionaries are used to describe multiple aspects of a single object. Like, say, a movie. Define a dictionary called movie that works with the following code.

movie = {
  'title': '10 Things I Hate About You',
  'year': 1999,
  'director': ' Gil Junger'
}

print("My favorite movie is", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director'])

# 2) On the lines after that, add keys to the movie dictionary for budget and revenue (you'll use code like movie['budget'] = 1000), and print out the difference between the two.

movie['budget'] = 30
movie['revenue'] = 53.5

# 3) If the movie cost more to make than it made in theaters, print "That was a bad investment". If the film's revenue was more than five times the amount it cost to make, print "That was a great investment." Otherwise print "That was an okay investment."

if movie['budget'] > movie['revenue']:
  print("That was a bad investment")
elif movie['revenue'] > movie['budget'] * 5:
  print("That was a great investment")
else:
  print("That was an okay investment")

# 4) Sometimes dictionaries are used to describe the same aspects of many different objects. Make ONE dictionary that describes the population of the boroughs of NYC. Manhattan has 1.6 million residents, Brooklyn has 2.6m, Bronx has 1.4m, Queens has 2.3m and Staten Island has 470,000. (Tip: keeping it all in either millions or thousands is a good idea)

population = {
  'Manhattan': 1.6,
  'Brooklyn': 2.6,
  'Bronx': 1.4,
  'Queens': 2.3,
  'Staten Island': 0.470
}

# 5) Display the population of Brooklyn.

print("The population of Brooklyn is", population['Brooklyn'])

# 6) Display the combined population of all five boroughs.

# Version 1: Access them manually
print("Total popuation is", population['Manhattan'] + population['Brooklyn'] + population['Bronx'] + population['Queens'] + population['Staten Island'])

# Version 2: Grab all of the values with .values()
print("Total population is", sum(population.values()))

# 7) Display what percent of NYC's population lives in Manhattan.
total_population = sum(population.values())
pct_manhattan = population['Manhattan'] / total_population * 100
pct_manhattan = round(pct_manhattan, 2)
print(pct_manhattan, "percent of NYC lives in Manhattan")