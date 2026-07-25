#Loops
'''
Loop control the flow of code
Repeat a block of code over and over until a condition is met

There are two types of loops 
For and while

#syntax of for loop is:
    for 'loop variable(usually 'i'; item maybe?)' in (sequence):
#behind the scene for loop creates a logic/process that it executes based on the sequence;python iterator
    Python iterator - an object that lets you go through items one by one in a sequence
    Remember whats done. Knows whats next
#then write the block of code should be repeated. So:
    for i in (1,2,3):
        print(i)

Output will be printed in each line:
1
2
3

#Example
for i in (1,2,3,4,5):
    #print("Round:", i); this line I wrote
    print(f"Round: {i}") #this Baraa wrote

#General rule for 'for loop': use same singular varaible name and plural sequence name 
#Example
items = (1,2,3,4,5) #this sequence is a tuple
for item in items:
    print(f"Round: {item}")

#a string is sequence of values
#sequence must have a start and end
#Sequence can be tuple, list, string, range
#range(stop); start is optional, it starts from zero by default in this case, and step is also optional. 
    range(start, stop, step); step is 1 by default

#use cases of for-loop
#1) We use for loops to go through values and aggregate data like summing, counting, or averaging
#Example
scores = [80, 50, 60, 75]
total = 0
for score in scores:
    #total = total + score
    total += score
    print("Current Total:", total)
print("Final total", total)

#2) We use for loops to transform data like cleaning data before processing
#Example
files = [' Report.csv ', 'DATA.csv ', ' final.TXT']
for file in files:
    file = file.strip().lower().replace('.txt', '.csv')
    print(f"Processing {file}")
    #Always remember: Clean first, transform second -- always in that order

#1 Python Challenge
#Print the 7-times table from 1 to 10 using a for loop
for number in range(1,11):
    print(f"7 X {number} = {7 * number}")

#2 Python challenge
#Print a left-aligned pyramid of stars with 6 rows using a for loop
for star in range(1, 7):
    print(star * '*')

#Advanced for-loop
#Break Statement - it stops the loop immediately; it jumps out and ends the loop right away
#Example
names = ['john', 'maria', '', 'khalid']
for name in names:
    if name == '':
        print('Empty value detected!')
        break
    print(f'Name = {name}')

#Continue statement - It skips one loop cycle without stopping the loop
#Example
names = ['john', 'maria', '', 'khalid']
for name in names:
    if name == '':
        print('Empty value detected!')
        continue
    print(f'Name = {name}')
#Use continue to skip bad or empty data without stopping the whole loop

#Pass statement = It is a placeholder where nothing happens; for now.. just keep going. Do nothing...
#Example
names = ['john', 'maria', '', 'khalid']
for name in names:
    if name == '':
        pass #todo: Handle Empty Value
        #later maybe handle the todo and do write below code for example
        #name = name.replace('', 'unknown')
    print(f'Name = {name}')

#Task: Skip weekends in calender loop
days = ['Mon', 'Sun', 'Wed', 'Tue']
weekends = ['Sat', 'Sun'] #created this inorder to avoid hardcoding values inside for or if. Instead, define them as variables
for day in days:
    if day in weekends: #added weekends instead of harcodeing ['Sat', 'Sun']
        continue
    print(f'Workday: {day}')

#Task: Scan emails to block unsafe data from entering your system
emails =[
    'data@gmail.com',
    'baraa@outlook.de',
    'DROP TABLE USERS;',
    'maria@gmail.com'
]

for email in emails:
    if ';' in email:
        print('SQL Injection: Hacker Attack') #hackers using sql injection to hack, one of the easiest ways baraa says
        break
    print(f'Processing Email: {email}')
'''

































































