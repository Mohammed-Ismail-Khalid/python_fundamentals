#Python Strings
#String Functions Categories

"""
text = 'hi'
number = 10
"""
'''
#print(type(text)) # <class 'str'>
#print(type(number)) # <class 'int'>
print(text.upper()) # HI
print(number.bit_length()) # 4
'''

#Problem: Create 5 variables - each with a different data type
'''
1. Your age
2. Your height (with decimals)
3. Your name
4. Are you a student? (True/False)
5. Something with no value yet
'''

'''
age = 32
height = 5.4
name = "Khalid"
is_student = False
to_be_determined = None

print("Age is:", age, "My height is:", height, "My name is:", name, "Am I a student:", is_student, "Something with no value yet:", to_be_determined)
'''

#Adding for commit

#text = """Python is easy to learn.
#Python is powerful.
#Many people love python"""

#print(text)

#Transformation
#phone = "176-1234-56"
#print(phone.replace("-", " "))

#chain method
#price = "$1,299.99"
#print(price.replace("$", "").replace(",", "")) # 1299.99

#Python challenge
#Convert the messy phone number into a clean number format with only digits.

"""
number = "+49 (176) 123-4576"
print(number.replace("+", "00").replace(" ", "").replace("(", "").replace(")", "").replace("-", ""))
"""

"""
#f string - formatted string
name = "Sam"
age = 34
is_student = False
print(f"Person name is {name}, they are {age} years old, and student status is {is_student}.")

To perform calculations within an f-string, you can include expressions inside the curly braces. For example:
x = 5
print(f"The value of x is {x} and its square is {x**2}.")       
"""
"""
#Transformation
stamp = "2026-09-20 14:30"
print(stamp.split(" "))
print(stamp.split("-"))
"""
#Data extraction
#Indexes and Slicing
"""
text = "Python"

#Extrack the first character
print(text[0]) # P or text[-6] # P
#Extract the last character
print(text[5]) # n or text[-1] # n
"""
"""
date = "2026-09-20"
#Extrack the year
print(date[0:4]) # 2026
#print(date[:4]) # 2026

#Extrack the month
print(date[5:7]) # 09
#Extrack the day
#print(date[8:]) # 20
print(date[-2:]) # 20
"""
#Data cleaning



