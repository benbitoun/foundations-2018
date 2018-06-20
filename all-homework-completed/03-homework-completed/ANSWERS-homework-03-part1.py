numbers = [4, 5, 1, 10, 200, 34, 22, 19, 43, 56, 32, 11, 40, 82, 23, 43, 12, 65, 10]

# 1) Count how many numbers are in the list. Use a for loop, do NOT use len. 
# Loop through, incrementing count each time
count = 0
for number in numbers:
    count = count + 1
print("There are", count, "numbers")

# 2) Use a Python method to add a new number to the list. You can pick the number!

print("Old numbers list", numbers)
numbers.append(3)
print("New numbers list", numbers)

# 3) Count how many even numbers are in the list. Use a for loop.

# Loop through, only incrementing if the number is even (number % 2 == 0)

count = 0
for number in numbers:
    if number % 2 == 0:
        count = count + 1
print("There are", count, "even numbers")


# 4) Count how many values are above the mean and how many are below the mean. Use one for loop.

# We need two counters, one to keep track of above and one to keep track of below
# Use an if statement to increment the right one when we go through the loop
# We need to import statistics to get the mean, I save it to a variable because
# it will look nicer than if number > statistics.mean(numbers)

import statistics
mean = statistics.mean(numbers)
below_mean = 0
above_mean = 0
for number in numbers:
    if number > mean:
        above_mean = above_mean + 1
    elif number < mean:
        below_mean = below_mean + 1

print("There are", above_mean, "numbers above the mean")
print("There are", below_mean, "numbers below the mean")

# 5) Total up the numbers. Use a for loop, do NOT use sum().

total = 0
for number in numbers:
    total = total + number
print("The total is", total)

# 6) Total up the numbers that are above the mean, and total up the numbers below the mean. Use one for loop, and do not use sum().
# Same thing we did with counting, except totaling this time
# We don't need to import again because we already did it, but I'm
# calculating the mean again just so we remember where it came from
# Maybe I should have called these above_mean_total and below_mean_total?

mean = statistics.mean(numbers)

above_total = 0
below_total = 0

for number in numbers:
    if number > mean:
        above_total = above_total + number
    elif number < mean:
        below_total = below_total + number

print("Above mean total: ", above_total)
print("Below mean total: ", below_total)

# 7) Find the largest number. Use a for loop.
# Assume the largest is the first one
# THen loop - look at each number, if it's larger than
# what we've seen already, then now it's the new largest
largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number


# 8) You have a list of dogs, shown below. BUT YOU GOT ANOTHER DOG!!! His name is Maxwell, please add him to the list.

dogs = ["Sparky", "Jane", "Matilda", "Blartsburg"]
print("Original dogs list is", dogs)

dogs.append("Maxwell")
print("New dogs list is", dogs)

# 9) Make a list of all dogs that have names of 5 characters or less. Use a for loop.

short_dog_names = []
for dog_name in dogs:
    if len(dog_name) <= 5:
        short_dog_names.append(dog_name)

print("Short dog names are", short_dog_names)

# 10) I'm on a web page with some links about Zurich, and the URL looks like this: http://important-swiss-things.ch/docs/download/ZH (no, it isn't a real URL). Bern is another canton - its abbreviation is BE, so its URL is http://important-swiss-things.ch/docs/download/BE.

# I want to get this link for every single canton in Switzerland, not just Zurich and Bern, BUT I don't want to type each URL manually. If I give you this list of the canton abbreviations, can you print out all of the URLs?

cantons = [ "ZH", "BE", "LU", "UR", "SZ", "OW", "NW", "GL", "ZG", "FR", "SO", "BS", "BL", "AR", "AI", "SG", "GR", "AG", "TG", "TI", "VD", "VS", "NE", "GE", "JU"]

# VERSION ONE: I think this one is more flexible/more readable
base = "http://important-swiss-things.ch/docs/download/"
for canton in cantons:
    print(base + canton)

# VERSION TWO: I think this one is less readable/less flexible
for canton in cantons:
    print("http://important-swiss-things.ch/docs/download/" + canton)

# 11) I'm trying to get some top-secret documents from top-secret-secrets.com, and while I know the URL pattern I don't want to type them all out individually!
# 
# Each secret document has a document ID and is made up of 12 pages, pages "001.pdf" through "012.pdf". Each page is available at a different URL. For example, for the document ID of QQ7LTHM, the pages are available at
# 
#     www.top-secret-pdfs.com/content/secrets/QQ7LTHM/page/001.pdf
#     www.top-secret-pdfs.com/content/secrets/QQ7LTHM/page/002.pdf
#     www.top-secret-pdfs.com/content/secrets/QQ7LTHM/page/003.pdf
#     ...
#     www.top-secret-pdfs.com/content/secrets/QQ7LTHM/page/012.pdf
#
# I have the following document IDs:
# 
#     qq7lthm
#     jemsqhg
#     O6itcke
#     cp4Iua0
#     bkijcmo
#     ctoyjrm
#     z8wc6xy
#     zk4Bmm0

# Can you print out all of the URLs? Note that the document IDs need to be capitalized in the URL, and it's "001.pdf" and "012.pdf", not "1.pdf" and "12.pdf".

# VERSION ONE
ids = ['qq7lthm','jemsqhg','O6itcke','cp4Iua0','bkijcmo','ctoyjrm','z8wc6xy','zk4Bmm0']
pages = ["001.pdf", "002.pdf", "003.pdf", "004.pdf", "005.pdf", "006.pdf", "007.pdf", "008.pdf", "009.pdf", "010.pdf", "011.pdf", "012.pdf"]

for id in ids:
    for page in pages:
        print("www.top-secret-pdfs.com/content/secrets/" + id.upper() + "/page/" + page)

# VERSION TWO: Use string formatting and range
# range(1,12) counts from 1 to 12 for you, just like creating [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# The :03d means "it's a decimal, make it 3 characters long with zeroes in front"
for id in ids:
    for page in range(1, 12):
        url = "www.top-secret-pdfs.com/content/secrets/{id}/page/{page:03d}.pdf".format(id=id.upper(), page=page)
        print(url)
