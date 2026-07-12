#Control Flow 
#Zero in boolean is false
#if we have some value in boolean then it shows True when print
#print(bool("A"))
"""

#any and all functions
email = ""
phone = "017-1234"
username = "baraa123"
#Allows registration
#if any field is filled
print(any([email, phone, username]))

#Allow registration
#only of all fields is filled
print(all([email, phone, username])) #all values should be true inorder to be true

#Comparision Operator
#print(10 != 10)
#strings can be compared too, alphabetically. Also case sensitive
#chained comparision, left to right
print(5 < 4 < 6) #everything should be true

#is age between 18 and 30?
age = 20
print(18 <= age <= 30)

#logical operations
print(3 > 1 and 5 < 1)
print(3 > 1 and 5 > 1)

print(3 > 1 or 5 > 1)
print(3 < 1 or 5 < 1)

#checks if the system is under pressure
cpu_usage = 70
memory_use = 95
print(cpu_usage > 90 or memory_use > 90)

#checking user credentials before login
email = True
password = False
print(email and password)

#not operator(it changes the reality of the operator so to speak)
print(not 3 > 2)
print(not True)
print(not not True)

#Control Mixed Conditions
#"and" operator has high priority
#parentheses has even higher priority
print((5 == 5 or 8 > 5) and 6 < 4)

#Example
#Allow access only if the user is logged in
#or they are a guest
#but they must not be banned

is_logged_in = True
is_guest = False
is_banned = True

#print(is_logged_in or is_guest and not is_banned) #when banned it should show false but the logic needs to be corrected here
print((is_logged_in or is_guest) and not is_banned)

#Membership (in) and (not in) operator
#print("a" in "data")
print("a" not in "data")
print(3 not in [1,2,3])

#Task
#Security check: ensure the domain is not banned
domain = "gmail.com"
banned_domains = ["spam.com", "fake.org", "bot.net"]
print(domain not in banned_domains)

#Identity (is) operator
#When variables are stored in memory, lets say a and b; here a will be assigned an ID(ex 30) and b(ex 40)
#so in memory :"a" is variable name, 40 is its ID in memory and whatever value is in the variable "a"
a = [1,2,3]
b = [1,2,3]
#to compare values, we use ==
print(a == b) #shows True
#to check wheather something is pointing to the same object, we check ID by using 'is' operator
print(a is b) #is a same object as b

#Example
x = ["a", "b", "c"]
y = x

print(x == y)
print(x is y)

#Make sure the email exits, and it's not empty

email = None
#print(email != None and email != "")
#here when dealing with 'None" best practise is to use "is" operator
print(email is not None and email != "")

#Python challenges
#1) Check if a user's name is not empty and the age is greater than or equal to 18

user_name = 'Khalid'
age = 18
print((not user_name == "") and age >= 18)

#2) Check if the password is at least 8 characters long and does not contain space
password = "12345 678"
print (len(password) >= 8 and " " not in password)

#3) Check if a users email is not empty, contains '@', and ends with '.com'
user_email = 'iszabikhalid@gmail.com'
#print(user_email[-4:])
print(not user_email == '' and "@" in user_email and user_email[-4:] == ".com")

#4) Check if a username is a string, is not None, and is longer than 5 character
user_name = "Khalid"
print(type(user_name) == str and user_name is not None and len(user_name) > 5)
"""
#5) Check if the user is either an admin or a moderator, and either they're not banned or they've verified their email.
user = input("Are you an admin or moderator?: ").lower()
user_email = input("Email please?: ").lower()
user_type = ["admin","moderator"]
check_user_type = user in user_type

user_banned = False
user_eamil_verified = "@" and ".com" in user_email

print((user is not None and check_user_type) and (user_banned or user_eamil_verified))



