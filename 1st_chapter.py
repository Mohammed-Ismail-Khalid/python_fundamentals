'''
# Data types
a = 10 #int
b = 3.14 #float
c = "Hello, World!" #string 
d = True #boolean
e = [1, 2, 3, 4, 5] #list
f = (1, 2, 3, 4, 5) #tuple
g = {"name": "John", "age": 30} #dictionary
h = {1, 2, 3, 4, 5} #set
i = None #NoneType
'''

#Do something to the data
#do something = fucntions
#data = values
#value -> Functions -> output(new value)

'''
Functions are blocks of code that perform a specific task and can be reused throughout your program. They take input values (arguments), process them, and return an output value.  
Independent block of code that can be called multiple times with different inputs to perform a specific task. Functions help in organizing code, improving readability, and promoting code reusability. 

Methods are functions that are associated with objects and can be called on those objects. They are defined within a class and operate on the data contained within the object. Methods are used to perform actions or manipulate the state of an object.   
Methods are functions belongs to a specific object or class and are called using the dot notation. They can access and modify the object's attributes and perform operations specific to that object.   
'''
text = 'hi'
number = 10
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
"""
"""
#Transformation
stamp = "2026-09-20 14:30"
print(stamp.split(" "))
"""

#with this chapter one ends