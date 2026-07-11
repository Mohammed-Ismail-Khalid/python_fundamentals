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

#not operator
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
"""











