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
"""
#Data cleaning
#white space cleanup
white_space_example = " Engineering"
print(white_space_example.lstrip()) # Engineering
white_space_example = "Engineering "
print(white_space_example.rstrip()) # Engineering
white_space_example = "       Engineering "
print(white_space_example.strip()) # Engineering

#specify the character to remove
example = "##AAA###"
print(example.strip("#")) # AAA

#next level
text = "    Engineering"
print(len(text)) 
print(len(text.strip()))

#to check how many white spaces removed
no_of_whitespaces = len(text) - len(text.strip())
is_my_data_clean = len(text) == len(text.strip())

print("Is my data clean?:", is_my_data_clean)
print("Number of white spaces to be removed:", no_of_whitespaces)

#case conversion
search = "Email ".lower().strip()
data = " emAil".lower().strip()

print(search == data)

#Python Challenge
#Turn the messsy sstring into a single clean summary with name, role, and age
messy_string = "968-Maria, ( D@t@ Engineer );; 27y  "
#output should be - name: maria | role: data engineer | age: 27

name = messy_string[4:9].lower()
role = messy_string[13:26].lower().strip("()").replace("@", "a")
age = messy_string[-6:-3]

print(f"name: {name} | role: {role} | age: {age}")

#string seaching
phone = "+48-176-12345"
print(phone.startswith("+49"))

email = "baraa@outlook.com"
print(email.endswith("gmail.com"))

print("@" in email)

url = "https://api.company.com/v1/data"
print("/api" in url)

#.find method gives the index of the first occurrence of a substring in a string. If the substring is not found, it returns -1.

phone1 = "+48-176-12345"
phone2 = "48-654-16548"
phone3 = "0048-654-16548"
#print(phone1.find("-")) # 3
print(phone1[phone1.find("-")+1:])
print(phone2[phone2.find("-")+1:])
print(phone3[phone3.find("-")+1:])

#checking and validating string
country = "USA"
#country = "USA#"
print(country.isalpha())

phone = "4748409498490"
#phone = "47-48409498490"
#phone = "3.14" #here . is consdered a special character, so it will return False
print(phone.isnumeric())
"""