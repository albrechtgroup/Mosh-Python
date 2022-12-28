# One Hour Python! - codeWithMosh.com
# Printing a string:
print("Hello World!!!")

# Declare variables: So that we can re-use. 'greet'
greet = print("Hello World!!!")
age = 33

print(age) # 33
# Changing the variable:
age = 42.75
print(age)

# Under_score variable names in Python:
first_name = "Mozart"

# Boolean value's Capitalized: True or False
onLine = True
print(onLine) # True

#######################
# Exercise:
# We check in a patient named John Smith.
patient = "John Smith"
# He is 20 years old.
age = 20
# He is a new patient.
newPatient = True
#######################

# input() receives info from the user:
name = input("What is your name? ")
# Below is string 'concatination':
print("Hello " + name)

# Type Conversion:
birth_year = input("Enter your birth year: ")
# int() turns the string into a integer
age = 2023 - int(birth_year)
print(age)

# float() turns the integer into a float
my_age = 42
print(float(my_age)) # 42.0

first = input("First: ")
second = input("Second: ")
sum = float(first) + float(second)
print("Sum equals: " + str(sum))

# string .methods():
course = 'Coding with Mosh'
print(course.upper()) # CODING WITH MOSH
# does Not change the variable
print(course) # Coding with Mosh

# Declaring a variale Will change. Make a copy.
lowerCase = print(course.lower())

# 'in' operator: Returns Boolean value:
print('Python' in course) # False
print('Mosh' in course) # True

favNumbers = [1, 3, 7, 13]
print(11 in favNumbers) # False

# Arithmetic Operators:
# + - * /

# Comparison Operators:

# Logical Operators:
# and - like the & in JS:
price = 25
print(price > 10 and price < 30) # True

# or - like the || in JS: Only one needs to be True

# not - like the ==! in JS:
# inverses/reverses any value given: Not True is, False

# 'if' statements:
# In Python, indentations serve as a block of code
# Vs. the {} in JS
temperature = 23
if temperature < 33:
    print("It is pretty darn Cold out here!")
    print("Better grab a coat.")
print("'OUTSIDE' of the 'if' statement block*")

# 'elif'statements:
temp = 97
if temp < 33:
    print("It is pretty darn Cold out here!")
    print("Better grab a coat.")
elif temp > 70 and temp < 90:
    print("It is Beautiful out here!!!")
elif temp > 33 and temp < 77:
    print("It's OK outside.")
else:
    print("I'm NOT going Out today :(")
# I'm NOT going Out today :(

# 'while' loops:
n = 1
while n <= 7:
    print(n)
    n = n + 1

# "Dollar Tree"
i = 1
while i <= 13:
    print(i * '$')
    i = i + 1
 
 # Lists:
names = ["Jona", "Less", "Mosh", "Sam", "Mary"]
print(names[2]) # Mosh
print(names)

# Update 1st name in 'names'
names[0] = "Dick"
print(names)  # ["Dick", "Less", "Mosh", "Sam", "Mary"]

# Print only a select. of the list:
print("================")
print(names[0:2]) #  
print("================")

rides = ["Mongoose", "Specialized", "Giant"]
print(rides)  # ["Mongoose", "Specialized", "Giant"]

newestBike = rides[2]
print(newestBike) # Giant

# List methods:
# .append() - will add to the End of the list
rides.append("VE1 Pro")
print(rides)  
# ['Mongoose', 'Specialized', 'Giant', 'VE1 Pro']
favoriteRide = rides[3]
print("*** " + favoriteRide + " ***")

# 'for' loops:
for ride in rides:
    print(ride)
# Mongoose
# Specialized
# Giant
# VE1 Pro

print("========================")
# Much clunkier way using 'while' and len() method:
i = 0
while i < len(rides):
    print(rides[i])
    i = i + 1

# The range() function:
numbers = range(7)
for number in numbers:
    print(number)

# Print 1-10
ratings = range(1, 11)
for rating in ratings:
    print(rating)

# Tuples: are Immutable(Unchangable) lists.
# [] - define lists. () - define tuples.




