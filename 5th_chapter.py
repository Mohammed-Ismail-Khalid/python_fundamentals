#Conditional Statments
"""
#if can be standalone
score = 100
if score >= 90:
    print("A")

#else can have no conditions, is optional but always need if statment   

score = 50
if score >= 90:
    print("A")
else:
    print("F")

#elif and nested if i have good enough understanding
score = 50
submitted_project = True
if score >= 90:
    if submitted_project:
        print("A+")
    else:
        print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

#using conditional operators
score = 60
submitted_project = False
if score >= 90 and submitted_project:
    print("A+")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60 or submitted_project:
    print("D")
else:
    print("F")

#mutliple if statments, they are independent
score = 100
submitted_project = False

if score >= 90:
    print("High Score")
else:
    print("Low Score")

if submitted_project:
    print("Project is submitted")
else:
    print("Project is not submitted")

#Inline if & Match case
#Inline must include else, and it doesnt have elif and can be stored in a variable
#only used when logic is simple
#Ex
score = 100
'''
if score >= 90:
    print("A")
else:
    print("F")
'''
'''
#The above code can be written as
grade = "A" if score >= 90 else "F"
print(grade)
'''

#since we cant use elif, theres one way to get the same result
'''
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("F")
'''
'''
#next level
grade = ("A" if score >= 90 else "B" if score >= 80 else "F") #from here if you add more it doesnt look good and make sense so use classical if statment
'''

#Match case; really new: can only be used for matching values

country = "India"
'''
#Normal eg
if country == "United States":
    print("US")
elif country == "India":
    print("IN")
elif country == "Egypt":
    print("EG")
elif country == "Germany":
    print("De")
else:
    print("Unknown Country")
'''
#Match ones
match country:
    case "United States" | "USA": #| is used to match mutiple values in a single case
        print("US")
    case "India":
        print("IN")
    case "Egypt":
        print("EG")
    case "Germany":
        print("DE")
    case _: # _ is like 'else'
        print("Unknown Country")
"""
#1 Python challenge
'''
Validate the Quality and Correctness of Email Values
- Must not be emtpy
- Must contain '.' and '@'
- Must contain exactly one '@' symbol
- Must end with '.com', '.org', or '.net'
- Must not be longer than 254 characters
- Must start and end with a letter or digit


email = "iszabikhalid@gmail.com"
#ending_email = ['.com', '.org', '.net']
email = email.strip()

if email == "":
    print("email must not be empty")
if not ('.' in email and '@' in email):
   print("Must contain '.' and '@'")
if email.count('@') > 1:
        print("email must contain only one '@")
if not email.endswith(('.com', '.org', '.net')):
        print("email must end with '.com', '.org', or '.net'")
if len(email) > 254:
        print("email must not be longer than 254 characters")
if not(email[0].isalnum() and email[-1].isalnum()):
        print("email must start and end with a letter or digit")
else:
    print("email is valid")

#2 Python Challenge
Validate the Quality and Correctness of Password
- Must not be empty
- Must be at least 8 characters
- Must include at least 1 uppercase
- Must include at least 1 lowercase
- Must not be same as the email
- Must not contain any spaces
- Must start and end with a letter or digit

email = "iszabikhalid@gmail.com"
password = "Ismail@w2043t"

if password == "":
    print("Must not be empty")
if not len(password) >= 8:
    print("Must be at least 8 characters")
if password == password.upper():
    print("Must include at least 1 uppercase")
if password == password.lower():
    print("Must include at least 1 lowercase")
if password == email:
    print("Must not be same as email")
if password.count(" ") > 0:
    print("Must not contain any spaces")
if not (password[0].isalnum() and password[-1].isalnum()):
    print("Must start and end with a letter or a digit")
else:
    print("Password is Valid")
'''




