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

#Unpacking Lists
person = ['Maria', 29, 'Data Engineer', 'Spain']
#name = person[0]
#age = person[1]
#role = person[2]
#country = person[3]

#Unpacking the list into variables
name, age, role, country = person #unpacking is a way to assign the values of a list to multiple variables in a single line of code. It allows for more concise and readable code, especially when dealing with lists that contain multiple values. The number of variables on the left side of the assignment must match the number of elements in the list being unpacked. If there are more elements in the list than variables, a ValueError will be raised. Similarly, if there are fewer elements in the list than variables, a ValueError will also be raised.
print(name) # output: 'Maria'
print(age) # output: 29
print(role) # output: 'Data Engineer'
print(country) # output: 'Spain'

name, *details, country = person #unpacking with the * operator allows for capturing multiple values from a list into a single variable. In this case, the * operator is used to capture all values between the first and last elements of the list into the 'details' variable. This is useful when you want to unpack a list but don't know how many elements it contains or when you want to ignore certain elements.
print(name) # output: 'Maria'
print(details) # output: [29, 'Data Engineer'] - captures the middle elements of the list into a new list called 'details'
print(country) # output: 'Spain'

name, *details = person #unpacking with the * operator allows for capturing multiple values from a list into a single variable. In this case, the * operator is used to capture all values after the first element of the list into the 'details' variable. This is useful when you want to unpack a list but don't know how many elements it contains or when you want to ignore certain elements.
print(name) # output: 'Maria'
print(details) # output: [29, 'Data Engineer', 'Spain'] - captures all elements after the first element of the list into a new list called 'details'

*details, role, country = person #unpacking with the * operator allows for capturing multiple values from a list into a single variable. In this case, the * operator is used to capture all values before the last element of the list into the 'details' variable. This is useful when you want to unpack a list but don't know how many elements it contains or when you want to ignore certain elements.  
print(details) # output: ['Maria', 29] - captures all elements before the last element of the list into a new list called 'details'
print(role) # output: 'Data Engineer'
print(country) # output: 'Spain'
# Rules:
# we are allowed to use only one * operator in unpacking a list, and it can be used to capture multiple values from the list into a single variable. The * operator can be placed before or after the variable name, depending on whether you want to capture values before or after a certain element in the list. However, you cannot use multiple * operators in a single unpacking statement, as this would create ambiguity in how to assign the values to the variables.
# Nr. of variables must match the values exactly -- not less, not more
# * Asterisk colllects leftovers, and its fine if there are none
# You can unpack any sequence (list, tuples, strings, etc.). Anything that iterable
#Eg
numbers = 'Hi'

first, *rest = numbers #unpacking a string into variables using the * operator. The first character of the string is assigned to the 'first' variable, while the remaining characters are captured into the 'rest' variable as a list. This is possible because strings are iterable in Python, meaning they can be treated like a sequence of characters that can be unpacked into variables.
print(first) # output: 'H' - the first character of the string is assigned to the 'first' variable
print(rest) # output: ['i'] - the remaining characters of the string are captured into the 'rest' variable as a list

#skipping items in unpacking 
person = ['Maria', 29, 'Data Engineer', 'Spain']
name, _, role, _ = person #unpacking a list into variables while skipping certain elements using the underscore (_) as a placeholder. The underscore is a convention in Python to indicate that a value is being ignored or not used. In this case, the second and fourth elements of the 'person' list are skipped, and only the first and third elements are assigned to the 'name' and 'role' variables, respectively. and it will be stored in memory
print(name) # output: 'Maria' - the first element of the list is assigned to the 'name' variable
print(role) # output: 'Data Engineer' - the third element of the list is assigned to the 'role' variable
#unlike the * operator, which captures multiple values into a single variable, the underscore is used to ignore specific values in the unpacking process. This is useful when you want to extract only certain elements from a list while disregarding others.

name, *_, country = person #unpacking a list into variables while skipping certain elements using the underscore (_) as a placeholder. The underscore is a convention in Python to indicate that a value is being ignored or not used. In this case, the second and third elements of the 'person' list are skipped, and only the first and last elements are assigned to the 'name' and 'country' variables, respectively. The * operator is used to capture all values between the first and last elements of the list into the '_' variable, which is ignored.
print(name) # output: 'Maria' - the first element of the list is assigned to the 'name' variable
print(country) # output: 'Spain' - the last element of the list is assigned to the 'country' variable

# How to Explore and Analyze lists
numbers = [1, 5, 5, 2, 4, 3]
print("Max:", max(numbers)) # output: 5 - returns the maximum value in the list
print("Min:", min(numbers)) # output: 1 - returns the minimum value in the list
print("Sum:", sum(numbers)) # output: 15 - returns the sum of all values in the list
print("Length:", len(numbers)) # output: 6 - returns the number of elements in the list

print("All:", all(numbers)) # output: True - returns True if all elements in the list are truthy (non-zero, non-empty, etc.), otherwise returns False
print("All:", all([1, 0, 2])) # output: False - returns False because one of the elements (0) is falsy
print("All:", all(['a', '', 'b'])) # output: False - returns False because one of the elements (empty string) is falsy

print("Any:", any(numbers)) # output: True - returns True if any element in the list is truthy, otherwise returns False
print("Any:", any([0, 0, 0])) # output: False - returns False because all elements are falsy (zero)
print("Any:", any(['a', '', 'b'])) # output: True - returns True because at least one element ('a' or 'b') is truthy

print("Count:", numbers.count(5))
print("Index:", numbers.index(5))

print(4 in numbers)
print(8 not in numbers)

list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(list1 == list2) # output: True - checks if the values of the two lists are equal
print(list1 is list2) # output: False - checks if the two lists are the same object in memory (they are not, even though they have the same values)

#Changing/Modifying a list
#1) adding items
#2) removing items
#3) updating items

#1) add item
letters = ['a', 'b', 'c', 'd']
#append() method adds an item to the end of the list. It takes a single argument
#letters.append('x')
#letters.append('y')

#insert() method adds an item at a specific index in the list. It takes two arguments: the index where the item should be inserted and the item itself.
#letters.insert(0, 'x') #inserts 'x' at index 0, shifting all other elements to the right
#letters.insert(3, 'y') #inserts 'y' at index 3, shifting all other elements to the right
#print(letters) # output: ['x', 'a', 'b', 'y', 'c', 'd'] - the list now contains the newly added elements at the specified indices

#Adding matrix

matrix = [['a', 'b', 'c'],  # Row 0
          ['d', 'e', 'f'],  # Row 1
          ['g', 'h', 'i']   # Row 2
          ]

#matrix.append(['x', 'y', 'z']) # appends a new row ['x', 'y', 'z'] to the end of the matrix
#print(matrix) # output: [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['x', 'y', 'z']] - the matrix now contains the newly added row at the end
#matrix.insert(0, ['a', 'a', 'a']) # inserts a new row ['a', 'a', 'a'] at index 0, shifting all other rows down
#print(matrix) # output: [['a', 'a', 'a'], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['x', 'y', 'z']] - the matrix now contains the newly added row at the specified index
#print(matrix) # output: [['a', 'a', 'a'], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['x', 'y', 'z']] - the matrix now contains the newly added rows at the specified indices

matrix[1].append('x') # appends 'x' to the second row of the matrix
print(matrix) # output: [['a', 'b', 'c'], ['d', 'e', 'f', 'x'], ['g', 'h', 'i']] - the second row of the matrix now contains the newly added element 'x' at the end
matrix[0].insert(0, 'z') # inserts 'z' at index 0 of the first row of the matrix, shifting all other elements to the right
print(matrix) # output: [['z', 'a', 'b', 'c'], ['d', 'e', 'f', 'x'], ['g', 'h', 'i']] - the first row of the matrix now contains the newly added element 'z' at the beginning


#change/remove items in the list
#Remove
letters = ['a', 'b', 'c']
#letters.clear() # removes all elements from the list, leaving it empty
#print(letters) # output: [] - the list is now empty

#letters.remove('a') # removes the first occurrence of 'a' from the list
#print(letters) # output: ['b', 'c'] - the list now contains only the elements 'b' and 'c', with 'a' removed 

#removed = letters.pop() # removes and returns the last element of the list
#removed = letters.pop(1) # removes and returns the element at index 1 of the list
#print(letters) # output: ['a', 'b'] - the list now contains only
#print("Removed Item:", removed)

#Removing matrix
matrix = [['a', 'b', 'c'],  # Row 0
          ['d', 'e', 'f'],  # Row 1
            ['g', 'h', 'i']   # Row 2
            ]

#matrix.remove(['a', 'b', 'c']) # removes the first occurrence of the row ['a', 'b', 'c'] from the matrix
#print(matrix) # output: [['d', 'e', 'f'], ['g', 'h', 'i']] - the matrix now contains only the rows ['d', 'e', 'f'] and ['g', 'h', 'i'], with the first row removed

#matrix.pop() # removes and returns the last row of the matrix
#print(matrix) # output: [['a', 'b', 'c'], ['d', 'e', 'f']] - the matrix now contains only the first two rows, with the last row removed

#matrix[1].remove('e') # removes the first occurrence of 'e' from the second row of the matrix
#print(matrix) # output: [['a', 'b', 'c'], ['d', 'f'], ['g', 'h', 'i']] - the second row of the matrix now contains only the elements 'd' and 'f', with 'e' removed 

matrix[-1].pop(0) # removes and returns the first element of the last row of the matrix
matrix[0].pop() # removes and returns the last element of the first row of the matrix
print(matrix) # output: [['a', 'b'], ['d', 'e', 'f'], ['h', 'i']] - the first row of the matrix now contains only the elements 'a' and 'b', with 'c' removed, and the last row of the matrix now contains only the elements 'h' and 'i', with 'g' removed   

#change your list - update items in the list
#update
letters = ['a', 'b', 'c']
letters[0] = 'x' # updates the first element of the list to 'x'
letters[1] = 'y' # updates the second element of the list to 'y'
#letters = 'z' #gotta be careful, this will change the list to a string, not a list anymore 
#print(type(letters)) 

#update matrix
matrix = [['a', 'b', 'c'],  # Row 0
          ['d', 'e', 'f'],  # Row 1
          ['g', 'h', 'i']   # Row 2
        ]

matrix[-1] = ['x', 'y', 'z'] # updates the last row of the matrix to ['x', 'y', 'z']
matrix[0][0] = '-'
matrix[1][1] = '-' # updates the second element of the second row of the matrix to '-'
matrix[-1][-1] = '-' # updates the last element of the last row of the matrix to '-'    
print(matrix) # output: [['-', 'b', 'c'], ['d', '-', 'f'], ['x', 'y', '-']] - the matrix now contains the updated values in the specified positions 

#Sorting list
letters = ['c', 'a', 'b']
#letters.sort() # sorts the list in ascending order, meaning to smallest to biggest
letters.sort(reverse = True) # sorts the list in descending order, meaning from biggest to smallest

print(letters) # output: ['c', 'b', 'a'] - the list is now sorted in descending order

#Sorting matrix
matrix = [['d', 'e', 'f'],  # Row 0
          ['g', 'h', 'i'],  # Row 1
          ['a', 'b', 'c']   # Row 2 
]

matrix.sort() # sorts the matrix in ascending order based on the first element of each row
print(matrix) # output: [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']] - the matrix is now sorted in ascending order based on the first element of each row.  The sort() method modifies the original list in place and does not return a new list.
#if we have a similar first element in the rows, it will sort based on the second element, and so on.

#if we want to sort based on a specific list
matrix = [['d', 'e', 'f'],  # Row 0
          ['a', 'z', 'i'],  # Row 1
          ['a', 'a', 'c']   # Row 2
]

matrix[1].sort()
print(matrix) #only second list got sorted

#sort the data without changing the original list
letters = ['c', 'a', 'b']
#new_list = sorted(letters) #keep the original list and create a clean and organised list
new_list = sorted(letters, reverse = True) #same is true for this function, it will reverse it
print('Orignal List:', letters)
print('Sorted list:', new_list) 

letters = ['c', 'a', 'b']
#if i dont care about the order of data just want to flip right to left then use reverse() method
letters.reverse()
print(letters)

letters = ['c', 'a', 'b']
#so inorder to keep the original list as is, then use this funtion
#new_list = reversed(letters) #this creates <list_reverseiterator object at 0x0000018DCDD2BA00>; an advanced topic; objects. So need to convert this into list
new_list = list(reversed(letters))
print('Original List:', letters)
print('Reversed Sorted List:', new_list)

#Copying List
#Assignement =
letters = ['a', 'b', 'c'] 
letters_copy = letters #this assignement will reference the same list in memory that means if i modify something here it will effect the orignal meaning no new copy of the same list is created inorder to work on it without consequences
letters_copy.append('z') #for eg this is effecting the original list
letters.pop() #removes the latest that means the last element
print('Original:', letters) 
print('Copy:', letters_copy)

#Shallow copy
letters = ['a', 'b', 'c'] 
letters_copy = letters.copy() #creates a container/list which is indepent of the origianl; creates a separate list in memory of the top level, meaning that only the parent list is independent, child elements will be pointed to the original hence can be effected by modification
letters.pop()
letters_copy.append('z')
print('Original:', letters) 
print('Copy:', letters_copy)

#Deep copy
#inorder to overcome shallow copy there is actually no built in function that can do that so need a separate copy module; imported
import copy
matrix = [['a', 'b'],  #Row 0
          ['c', 'd']  #Row 1
          ]

matrix_copy = copy.deepcopy(matrix) #Here copy. is module name. deepcopy() function creates a true, independent copy for all levels
matrix.pop()
matrix_copy[0].append('z') #add z to the first list
print('Original:', matrix)
print('Copy:    ', matrix_copy)
#note: deepcopy() function instead of it if you want shallow copy from this module use copy.copy()

#Testing 
#IS operator
import copy
original = [['a', 'b'],  #Row 0
          ['c', 'd']  #Row 1
          ]

#Asignment
copy1 = original
print("Same Object?", original is copy1, "\n")

#Shallow copy
copy2 = original.copy()
print("Same Object?", original is copy2)
print("Shared Lists?", original[0] is copy2[0], "\n")

#Deep Copy
copy3 = copy.deepcopy(original)
print("Same Object?", original is copy3)
print("Shared List?", original[0] is copy3[0], "\n")
#Tip: Use the 'is' operator to check if the copies are truly independent
#Avoid Assignment = (Risky and confusing)
#Use .copy() for simple, flat lists
#use copy.deepcopy() for Nested lists
#Always make extra copy for Experiments/Tests

#Combining Lists
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
#comb = letters + numbers  #add in one combined list
comb = [letters, numbers] #like matrix, nested list
print(comb)
#print(letters * 2)

#extend 
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
numbers.extend(letters)
print(letters)
print(numbers) #extend doesnt create a new list; it expands the orignial one

#combining using zip(); pairing elements from one to another list; creates tuple; stops at the shortest element pair
letters = ['a', 'b', 'c']
numbers = [1, 2, 3, 4]
#comb = zip(letters, numbers) #prints iterative object; <zip object at 0x00000249C65B9A40>, need to convert it into list using list()
#comb = list(zip(letters, numbers))
comb = list(zip(letters, numbers, "Hi")) #can be added like this add it will stop with two pairs
print(comb)

#Baraa own use case; Pair Customers with thier IDs (rebuild the relationship)
ids = [101, 102, 103]
names = ['Ali', 'Sara', 'John']
#print(ids + names) #output: [101, 102, 103, 'Ali', 'Sara', 'John'] ; doesnt make any sense
print(list(zip(ids, names))) #output: [(101, 'Ali'), (102, 'Sara'), (103, 'John')]
'''







