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

empty = list() # empty list using list() built-in function
print(empty) # output: []

letters = list('Python') # converts string to list of characters
print(letters) # output: ['P', 'y', 't', 'h', 'o', 'n']

numbers = list(range(5)) # creates a list of numbers from 0 to 4
print(numbers) # output: [0, 1, 2, 3, 4]

#Nested list matrix
matrix = [['a', 'b', 'c'], 
          ['d', 'e', 'f'], 
          ['g', 'h', 'i']] #best practice to use nested list for matrix representation

print(matrix) # output: [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
print(type(matrix)) # output: <class 'list'>

mixed_matrix = [[1, 2, 3], 
                ['a', 'b', 'c'], 
                [True, False, None]] # nested list with mixed data types

print(mixed_matrix) # output: [[1, 2, 3], ['a', 'b', 'c'], [True, False, None]]
print(type(mixed_matrix)) # output: <class 'list'>


#2) how to Read and Access elements from a list; Indexing and Slicing
#Indexing is a way to access individual elements in a list using their position or index. -- by vs code AI
#Important point to remember about Python:
#Python Automatically detect the data type of the variable based on the value assigned to it. This is known as dynamic typing. For example, if you assign an integer value to a variable, Python will automatically treat it as an integer. If you later assign a string value to the same variable, Python will treat it as a string. This allows for flexibility in programming, but it also means that you need to be careful about the types of values you are working with.
#Data types
#1) None - No value; used to represent the absence of a value or a null value. It is often used as a placeholder for optional or missing data. In Python, None is a built-in constant that represents the absence of a value or a null value. It is commonly used in functions that do not return a value, or as a default value for function arguments that are optional. For example, if a function does not have a return statement, it will return None by default. Similarly, if an argument is not provided when calling a function, it will be assigned the value of None.
#2) Single Value Data Types - int, float, bool, str, complex
#3) Collection Data Types - list, tuple, set, dict; also called Data Structures or container(s) data types; used to store multiple values in a single variable. They are used to group related data together and provide a way to organize and manipulate that data. Each collection data type has its own unique characteristics and methods for accessing and manipulating the data it contains.
#Access and Read
lst = ['a', 'b', 'c', 'd', 'e'] # list of letters
print(lst)
print(lst[0]) # output: 'a' - accessing the first element using index 0
print(lst[-2]) # output: 'd' - accessing the second last element using negative index -2

#Access and Read nested matrix
matrix = [['a', 'b', 'c'], # Row 0
          ['d', 'e', 'f'], # Row 1
          ['g', 'h', 'i'] # Row 2
]

#print(matrix)
print(matrix[2]) #or print(matrix[-1]) # output: ['g', 'h', 'i'] - accessing the last row using index 2 or -1
print(matrix[-1][2]) # output: 'i' - accessing the last element of the last row using negative index -1 and index 2
print(matrix[0][0]) # output: 'a' - accessing the first element of the first row using index 0 and index 0
print(matrix[1][-2]) # output: 'e' - accessing the second element of the second row using index 1 and index 1

#Slicing is a way to access a range of elements in a list using a start index, an end index, and an optional step value. The start index is inclusive, while the end index is exclusive. The step value determines the increment between indices. Slicing can be used to create a new list that contains a subset of the original list's elements. For example, lst[1:4] will return a new list containing the elements at indices 1, 2, and 3 of lst.
letters = ['a', 'b', 'c', 'd'] # list of letters
print(letters[:3]) # output: ['a', 'b', 'c'] - slicing from the beginning to index 2 (exclusive)
print(letters[2:]) # output: ['c', 'd'] - slicing from index 2 to the end

matrix = [['a', 'b', 'c'], # Row 0
          ['d', 'e', 'f'], # Row 1
          ['g', 'h', 'i'] # Row 2
]

print(matrix[:2]) # output: [['a', 'b', 'c'], ['d', 'e', 'f']] - slicing the first two rows
print(matrix[1:]) # output: [['d', 'e', 'f'], ['g', 'h', 'i']] - slicing from the second row to the end
print(matrix[2][:2]) # output: ['g', 'h'] - slicing the first two elements of the last row
'''


