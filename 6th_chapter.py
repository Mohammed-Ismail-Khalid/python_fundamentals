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

#Comparision of break, continue, and pass statements; when to use them:
#break - when Critical Risk: cost, security, integrity; Exit immediately
#Continue - Meduium rist: Bad rows, Empmty files/data, skip special cases
#pass - just keep doing what you are doing. I may have plan for this; placeholder

#Else in loops; Runs a block of code only if the loop finishes naturally
#Example: Check for even number
items = [1, 3, 4, 7]
for i in items:
    if i % 2 == 0:
        print("Even Nr. Found:", i)
        break
else: #should be on the same line as for; else is only used in this case where break is used
    print("All numbers are odd")

#for-else use cases; especially data validation and assurance
#Task: Check for Missing Names in a list
names = ['Kamara', 'Tuba', None, 'Mounika'] #instead of None use 'baraa' else statement will be executed

for name in names:
    if name is None:
        print('Found a missing name')
        break
else:
    print('All names are available')

#Task: Check if All Files are CSV Files
files = [
    'data1.csv',
    'report.pdf',
    'data2.txt'
    'report2.csv'
]

for file in files:
    if not file.endswith('.csv'):
        print('Not all files are CSV') #print(f'{file} is not CSV') if we have multiple files is useless to get all the desired output
        break #it makes no sense to use continue statement and apply else below
else:
    print('All files are CSV')

#Python Challenge
#Check whether any filename appeares more than once
#Print "Duplicate found" if a duplicate exists, otherwise print "All files are unique"
file_list = [
    'report.csv',
    'data.xlsx',
    'summary.docx',
    'report.csv',
    'data.csv'
]

#My wrong code
index = ''

for file in range(0, len(file_list)):
    index = index + file_list[file]
    if index == file_list[file + 1]:
        print("Duplicate found")
        break
else:
    print("All files are unique")
'''
'''
#Grok code which makes some sense to me
seen = set() #set is a collection that stores only unique values

for file in file_list:
    if file in seen:
        print(f"Duplicate found: {file}") #I added f string to show whats the dup
        break
    seen.add(file)
else:
    print("All files are unique")

#Another grok answer without set()

file_list = [
    'report.csv',
    'data.xlsx',
    'summary.docx',
    'report.csv',
    'data.csv'
]

# Make a sorted copy
sorted_files = sorted(file_list)

for i in range(len(sorted_files) - 1):
    if sorted_files[i] == sorted_files[i + 1]:
        print("Duplicate found")
        break
else:
    print("All files are unique")

#output:
#original list: report.csv → data.xlsx → summary.docx → report.csv → data.csv
#sorted list: data.csv → data.xlsx → report.csv → report.csv → summary.docx
#Now the two "report.csv" are next to each other, so the simple comparison catches them.

#Nested loop
#Example
for x in range(3): #outer loop
    for y in range(2): #inner loop
        for z in range(2):
            print(f"({x}, {y}, {z})")

#Nested loop use cases
#Crossing/Combining Data: All possible combinations
#Example
colors = ['red', 'blue', 'green']
sizes = ['L', 'M', 'S']

for color in colors:
    for size in sizes:
        print(f"{color} - Size {size}")

#Nested loop most use case: Navigate Hierarchy
years = [2026, 2027]
months = ['Jan', 'Feb']
days = range(1, 29)

for y in years:
    for m in months:
        for d in days:
            print(f"report_{y}_{m}_{d}.csv")

#data engineering/analyst use case; working with tables; sql quarry said baraa
#Example
# SELECT count(*) FROM customers where id IS NULL;
tables = ['coustomers', 'orders', 'products', 'prices']
columns = ['id', 'create_date']

for t in tables:
    for c in columns:
        print(f'SELECT count(*) FROM {t} WHERE {c} is NULL:')

#While loop
#Repeats a block of code - over and over as long as condition is True!
#in for loop we are iterating in a predefined sequence and predefined condition. 
#in while loop the code block is repeated as long as the condition is true. Involves risk!; Unknown times!
#while loop should have Initialization then condition then the initialzation should be updated

#Task: Build a counter from 1 to 5
count = 1 #initialization
while count <= 5: #condition
    print(count)
    count += 1 #update

#Task: Write a program that keeps askinig "Do you agree?" until the user types "yes"
answer = ""
while answer != "yes":
    answer = input("Do you agree?(yes/no): ")
print("Thank you")
'''

















































