#Python Numbers
#Numeric has 3 types: int, float, complex
"""
x = 5
y = 5.7
z = 2 +3j

print(type(x))
print(type(y))
print(type(z))

#Math operators
print(7 //2) #floor division means round number
print(10 % 2) #modulus means remainder. Used for even or odd numbers

x = 2
#if we are adding x to itself then instead of writing x = x + 3 we can write x += 3
x += 3 #notice we are adding math operator before equal sign. This is called augmented assignment operator
print(x)
x -= 1
print(x)
x *= 2
print(x)

import math #since floor and useful functions are not built-in functions
#Rounding numbers
#measure distance
print(abs(2 - 10)) #absolute value

price = 35.68685698
print(round(price))
print(round(price, 2)) #rounding to 2 decimal places. That means round(number, ndigits)
print(math.floor(price))
print(math.ceil(price))
print(math.trunc(price)) #trunc cut out the decimals and give the exact number without decimals
#int vs trunc, trunc inorder to make sense because int is usually used for changing data types

#Random
import random
#random is used for dummy data generation
print(random.random()) #could give float
print(random.randint(1,6)) #randint(start, end)

#validation
#to check wheather a number when its digits could be hidden is an integer. In data engineering 
x = 7.0
print(x.is_integer()) #is_integer is a method thats why we are using .

y = 7.1
print(y.is_integer())

#isinstance(value, type) checks if a value belongs to a certain data type.  bool
x = 70.4
print(isinstance(x, int))
#Generate a random integer between 1 and 100, and check if the result is an even number
"""


