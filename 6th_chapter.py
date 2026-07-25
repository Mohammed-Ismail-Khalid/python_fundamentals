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
'''
#2) We use for loops to transform data like cleaning data before processing
#Example
files = [' Report.csv ', 'DATA.csv ', ' final.TXT']
for file in files:
    file = file.strip().lower().replace('.txt', '.csv')
    print(f"Processing {file}")
    #Always remember: Clean first, transform second -- always in that order





