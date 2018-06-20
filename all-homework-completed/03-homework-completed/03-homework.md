Here's another homework for you to refine your skills with! It's TOTALLY OPTIONAL, but will provide good practice. I'll review it on Friday.

Dn't worry if you find things to be magical, confusing, or difficult. You might know the concepts of lists and dictionaries, but getting them to do what you want is a lot of trouble. Doing things with lists and dictionaries is probably 60% of programming, so we'll be working on them for a while. You'll get plenty of practice!

For this homework, it's the same topics - lists and dictionaries - but instead of boring fake tasks, these are more focused on common techniques and patterns you'll see in the real world.

The first two parts are definitely easier than the Spotify part of Homework #2. The third part might be easier, too, since you're going to be more skilled now. Or it might be harder!

As always, just finish what you can.

HOMEWORK 3

Please create a new file named homework-3-lastname.py
The first line should be a comment with your full name
The second line should be the date
The third line should be a comment "Homework 3"

Submit by Friday at noon - that's when I'll review it.

PART ONE: Lists

There are a lot of common ways to deal with lists - maybe you're counting, totaling, or finding maximums or minimums. Sometimes when you want to count, or total, or find max/min, you don't care about the ENTIRE list, you only care about SOME of the list - maybe you want to total up the value of only red cars, or finding the fastest car built before 1965. The problems below will help you get there.

I have a litte writeup of common patterns at http://jonathansoma.com/lede/foundations-2018/classes/data%20structures/looping-patterns/ if you want some tips.

Most of the problems below have easy answers using Python functions like len(), max(), sum(), etc. To get practice with loops, though, I want you to try to solve the problems with them! It's stupid, but I think it will help you learn a little more about how loops work. Once you add in dictionaries  these skills will be very, very useful - it's nice to start with simpler data sometimes

    numbers = [4, 5, 1, 10, 200, 34, 22, 19, 43, 56, 32, 11, 40, 82, 23, 43, 12, 65, 10]

1) Count how many numbers are in the list. Use a for loop, do NOT use len. 

2) Use a Python method to add a new number to the list. You can pick the number!

3) Count how many even numbers are in the list. Use a for loop.

4) Count how many values are above the mean and how many are below the mean. Use one for loop.

5) Total up the numbers. Use a for loop, do NOT use sum().

6) Total up the numbers that are above the mean, and total up the numbers below the mean. Use one for loop, and do not use sum().

7) Find the largest number. Use a for loop.

8) You have a list of dogs, shown below. BUT YOU GOT ANOTHER DOG!!! His name is Maxwell, please add him to the list.

    dogs = ["Sparky", "Jane", "Matilda", "Blartsburg"]

Do NOT just edit the line to be ..., "Blartsburg", "Maxwell" ]

9) Make a list of all dogs that have names of 5 characters or less. Use a for loop.

10) I'm on a web page with some links about Zurich, and the URL looks like this: http://important-swiss-things.ch/docs/download/ZH (no, it isn't a real URL). Bern is another canton - its abbreviation is BE, so its URL is http://important-swiss-things.ch/docs/download/BE.

I want to get this link for every single canton in Switzerland, not just Zurich and Bern, BUT I don't want to type each URL manually. If I give you this list of the canton abbreviations, can you print out all of the URLs?

    cantons = [ "ZH", "BE", "LU", "UR", "SZ", "OW", "NW", "GL", "ZG", "FR", "SO", "BS", "BL", "AR", "AI", "SG", "GR", "AG", "TG", "TI", "VD", "VS", "NE", "GE", "JU"]

11) I'm trying to get some top-secret documents from top-secret-secrets.com, and while I know the URL pattern I don't want to type them all out individually!

Each secret document has a document ID and is made up of 12 pages, pages "001.pdf" through "012.pdf". Each page is available at a different URL. For example, for the document ID of QQ7LTHM, the pages are available at

    www.top-secret-pdfs.com/content/secrets/QQ7LTHM/page/001.pdf
    www.top-secret-pdfs.com/content/secrets/QQ7LTHM/page/002.pdf
    www.top-secret-pdfs.com/content/secrets/QQ7LTHM/page/003.pdf
    ...
    www.top-secret-pdfs.com/content/secrets/QQ7LTHM/page/012.pdf

I have the following document IDs:

    qq7lthm
    jemsqhg
    O6itcke
    cp4Iua0
    bkijcmo
    ctoyjrm
    z8wc6xy
    zk4Bmm0

Can you print out all of the URLs? Note that the document IDs need to be capitalized in the URL, and it's "001.pdf" and "012.pdf", not "1.pdf" and "12.pdf".

TIPS

Every looping question is built up of THREE parts
1. The Initial Condition
2. The Condition
3. The Update
What does that mean?! Learn more details one the site at http://jonathansoma.com/lede/foundations-2018/classes/data%20structures/looping-patterns/

Instead of always adding one to a number, maybe you should think about adding to a running total, or putting another element into a list.

When getting the mean and median, use the statistics package.

If you'd like to get fancy for the last one, you can look up formatting with "leading zeroes"

The document IDs I gave you are lowercase, but you need them to be capitalized!

PART TWO: Dictionaries

Dictionaries are super useful and you use them all of the time, but I wouldn't say there are very many 'tricks' like there are with lists. Most of the time you just want to put things in and take things out using keys.

1) Let's say we are terrible doctors and we have a patient. Define a dictionary called patient that works with the following code.
 
print("Doctor, it looks like the patient named", patient['name'], "is complaining about", patient['complaint'])
 
2) We aren't really listening to their complaint, but as more test results come in, we'll add these things to the patient's record. Add the following to the patient dictionary:

    Heart rate: 70
    Temperature: 98.6
    Infection: No

Do *not* create a new dictionary - each one of these should be added to the existing dictionary on a separate line.

3) Now let's be doctors! Diagnose the patient, and store your diagnosis in a key called 'diagnosis':

* If their temperature is above 102 but they do not have an infection, they have heat stroke.
* If they have a temperature above 102 and they have an infection, they have the flu.
* If they have an infection but a normal temperature, it's probably a cold.
* If none of the above, tell them to take an aspirin and call you in the morning.

When you are finished diagnosing the patient, display "Your diagnosis is _______."
 
4) Make a list of 3 different patients, each with different complaint, heart rate, temperature, and whether they have an infection or not (this will be a list of dictionaries). Use a for loop to diagnose each of them.

PART THREE: Reading CSV files

When you first start with Python, you might be dumb enough to use csv.DictReader to open CSV files (a csv is like a less fancy Excel spreadsheet). Unfortunately, right now we are all very very very dumb! In the future I will tell you the good, smart way, but for now let's use csv.DictReader to practice with lists and dictionaries.

    import csv

    csvfile = open('countries.csv', 'r')
    reader = csv.DictReader(csvfile)
    data = list(reader)
    csvfile.close()
    print("The data looks like", data)

When you run this code, it will open up a file and convert it into a list of dictionaries. Each row becomes a dictionary, and each column becomes a key. Not sure what I mean? Look at what we print out, or try to use a for loop to print out each row.

NOTE: With Python 3, reading in CSV files is friendlier than it used to be, and uses something called an "ordered dictionary." It means the keys have a specific order to them, but most importantly they don't have { } around them! They're still dictionaries, though.

Answer the following questions based on my favorite boring dataset, countries.csv.

1) What are the columns in our dataset?

2) How many countries do we have in our dataset?

3) How many countries in Asia? How about North America?

4) What is the total population of the world?

5) Which has a larger population, Africa or South America?

6) Calculate the total GDP of each country and print it out (right now it's per capita).

7) What is the median life expectancy of the world?

8) What is the median life expectancy of Europe?

9) Print out each country that has a below-average life expectancy.

10) Print out each country that has a below-average GDP but an above-average life expectancy.

11) Calculate the 75th percentile of GDP.

12) What percent of the world population has a life expectancy of below 50 years? Above 80 years?

TIPS

A quick way to find out the columns is to select the first dictionary and look at its keys.

You don't have to use a for loop for number two!

For most of these, you'll use the same approaches as you did with Part One and the lists, you just need to figure out which patterns are the right ones.

You know how to get a median if given a list of numbers. For some of these it might be helpful to use your for loop to create a new list of numbers, then calculate the median from it.

...for example, with "What is the median life expectancy of Europe?", you'll need to make a new list of only the life expectancies of Europe, then get the median of that list. You'll rely on .append for that (although I'll also teach you a method called list comprehensions).

You know how to calculate the 50th percentile - it's the median of ALL of the values. The 75th percentile should be the 50th percentile of only the top 50% of the values.