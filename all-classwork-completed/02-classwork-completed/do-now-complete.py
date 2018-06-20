# Reviewing: variables, command line, if/else

# 1) Given the code below, what is the output?

i = 5
print(5 * 5)
# 25
print(i)
# 5
print("cat" + "dog")
# catdog
print("cat", "dog")
# cat dog
print("I have", 5, "cats")
# I have 5 cats
print("I have" + "5" + "cats")
# I have5cats

# 2) The two lines of code below won’t work. What is wrong with each of them?

print(5, "5")

print("Hello")

# 3) What two things are wrong with this if statement? 

if n == 2:
  print("two")

# 4) What is the command to list the files in a directory? What is the command to go “up” one folder?


# ls
# ls -a
# dir

# 6) Given the code below, what would the outputs be for n = 10 and n = -5?

print(n)
if n > 0:
  print("A")
  if n >= 3:
    print("B")
    print("C")
  elif n > 2:
    print("D")
  else:
    print("E")
elif n > -2:
  print("F")
else:
  print("G")

if n < 5:
  print("H")



