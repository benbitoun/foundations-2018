# Do Now

# Reviewing: dictionaries, lists, for loops

# 1) I have a list called bubblegum. How do I get the first element? The last element?

bubblegum = [1, 2, 3, 4]
bubblegum[0]
bubblegum[-1]

# 2) What function or method…
# …tells how many elements are in a list?
# …replaces text in a string with other text?
# …gives you the keys of a dictionary?

len(bubblegum)
"lkmasdlkm".replace("lkm","XXXX")

a_dictionary_of_things.keys()


# 3) What is the output of the following code? Which lines give you errors?

borough_name = 'Manhattan'
z = [ 'Manhattan', 'Queens' ]
x = { 
  'borough_name': 'Manhattan',
  'population': 500
}
y = {
'Manhattan': 500,
'Queens': 200
}

print(x['borough_name']) # Manhattan
# print(x[borough_name]) # x['Manhattan'] KEY ERROR
# print(x[0]) KEY ERROR (not a list)
# print(y['borough_name'])# KEY ERROR, doesn't have that key
print(y[borough_name]) # y['Manhattan'] 500
# print(y[0])# KEY ERROR
print(z['borough_name'])
print(z[borough_name]) # z['Manhattan']
print(z[0]) # Manhattan

# 4)  Print out each art piece’s name. 

art_pieces = [
{ ‘title’: ‘Gold Star’, ‘year’: 1805 }, 
{ ‘title’: ‘Blunderbuss‘, ‘year’: 1800 },
{ ‘title’: ‘Chairlift’, ‘year’: 1976 },
{ ‘title’: ‘Rancor’, ‘year’: 2002 }
]

for piece in art_pieces:
  print(piece['title'])

# 5) Given the following, write code to calculate how many murders we have in total.

murders = { 
  'Albany': 23, 
  'Kings County': 10, 
  'Rochester': 7, 
  'Yonkers': 9
}


murders['Albany'] + murders['Kings County'] + murders['Rochester'] + murders['Yonkers']



murders.keys() 
[ 'Albany', 'Kings County', 'Rochester', 'Yonkers']

murders.values()
[23, 10, 7, 9]
sum(murders.values())

murder_numbers = [23, 10, 7, 9]
sum(murder_numbers)









