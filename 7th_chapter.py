#Data Structures is a way of organizing and storing data in a computer so that it can be accessed and modified efficiently. It provides a means to manage large amounts of data for use in databases, internet indexing services, and large-scale applications. Common data structures include arrays, linked lists, stacks, queues, trees, and graphs. Each data structure has its own strengths and weaknesses, making them suitable for different types of applications.
#Primitive data type; one variable one value; int, float, char, bool
#4 types of Data structures: Linear, Non-linear, Static, Dynamic (by built in AI in VS code)
#4 types of Data structures:
#1) list - common; sqare brackets; mutable meaning can be changed
#2) tuple - immutable meaning cannot be changed; parenthesis
#3) set - unordered collection of unique elements; curly braces
#4) dictionary - collection of key-value pairs; curly braces
# so in python we have standard library - Built-in Modules - 1)Functions: print(), input(), len(), type(), range(), etc. 2) <class 'list'>, <class 'tuple'>, <class 'set'>, <class 'dict'>, etc. 
# Function gives you a value once input is given, work is done and output is given; Function is a block of code that performs a specific task and can be reused multiple times in a program. It takes input, processes it, and returns an output. Functions help in breaking down complex problems into smaller, manageable parts, making the code more organized and easier to understand. In Python, functions are defined using the 'def' keyword followed by the function name and parentheses.
# where as Methods are functions that are associated with objects and can be called on those objects. They are defined within a class and can access and modify the object's attributes. Methods are used to perform operations on the data contained within an object, allowing for encapsulation and abstraction in object-oriented programming. In Python, methods are defined using the 'def' keyword within a class definition, and they typically take 'self' as their first parameter to refer to the instance of the class.(by vs code AI)
#first_list = [1, 2, 3, 4, 5] # list
'''
#Roadmap
1) create a list
2) how to access and read elements from a list
3) How to unpack a list
4) How to Explore and Analyze a list
5) How to Change/modify a list
6) How to order a list
7) How to copy a list
8) How to Combine
9) How to Iterate through a list
10) How to Transform a list
11) How to Filter a list
12) List Comprehension

#1) How to create a list
empty_list = [] # empty list
letters = ['a', 'b', 'c', 'd'] # list of letters
mixed_data_types = [1, 'a', 3.14, True, None] # list with mixed data types
print(empty_list) # output: []
print(type(empty_list)) # output: <class 'list'>
print(letters) # output: ['a', 'b', 'c', 'd']
print(type(letters)) # output: <class 'list'>
print(mixed_data_types) # output: [1, 'a', 3.14, True, None]
print(type(mixed_data_types)) # output: <class 'list'>
#For behind the scenes, read notes

#there is also a list built-in function called list() which can be used to create a list from an iterable object like a string, tuple, or set. For example:
string_to_list = list("hello") # converts string to list of characters
print(string_to_list) # output: ['h', 'e', 'l', 'l', 'o'] #by AI in VS code
'''
empty = list() # empty list using list() built-in function
print(empty) # output: []

letters = list('Python') # converts string to list of characters
print(letters) # output: ['P', 'y', 't', 'h', 'o', 'n']

numbers = list(range(5)) # creates a list of numbers from 0 to 4
print(numbers) # output: [0, 1, 2, 3, 4]
