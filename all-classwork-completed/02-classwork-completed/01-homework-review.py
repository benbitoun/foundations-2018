# When run from the command line, this file should

# 1. Prompt the user for their year of birth, and tell them (approximately):


year = int(input("What year were you born in?"))

year = input("What year were you born in?")
year = int(year)

# 2. How old the user is

age = 2018 - year

# 3. How many times the user's heart has beaten

heartbeats = age * 80 * 60 * 24 * 365

# 4. How many times a blue whale's heart has beaten

whale_heartbeats = age * 10 * 60 * 24 * 365

# 5. How many times a rabbit's heart has beaten

rabbit_heartbeats = age * 150 * 60 * 24 * 365

# 6. If the answer to (5) is more than a million, say "XXX million" instead of the very long raw number

if rabbit_heartbeats > 1000000:
  million_rabbits = round(rabbit_heartbeats / 1000000)
  print(million_rabbits, "million")

# 7. How old they are in Venus years

# 8. How old they are in Neptune years

# 9. Whether they are the same age as you, older or younger

my_age = 35

if age > my_age:
  print("You're older than me!")
  print(age - my_age)
elif age < my_age:
  print("You're younger than me!")
  difference = my_age - age
  if difference == 1:
    print("You are 1 year younger than me")
  else:
    print("You are", difference, "years younger than me")
  print(my_age - age)
else:
  print("We're the same age!")


# 10. If older or younger, how many years difference


# 11. If they were born in an even or odd year

# 12. Which US President was in office when they were born (1935 onward)





if 1935 <= year <= 1939:
  print("President Blubs")
elif 1940 <= year <= 1944:
  print("President Erds")
elif 1945 <= year <= 1949:
  print("President Drobs")
else:
  print("President Trump")

year = 1943

if year < 1940:
  print("President Blubs")
elif year < 1945:
  print("President Erds")
elif year < 1950:
  print("President Drobs")
else:
  print("President Trump")
