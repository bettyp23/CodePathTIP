# Stacks vs Queues
# Stacks and Queues are both special types of lists that maintain certain properties about insertion and removal order.

# Problems solved with a stack are often implement a recursive solution, because under the hood, computers use a stack data structure to track the sequence of recursive function calls. When we initiate a series of recursive calls, we are essentially making a stack. Every time a recursive call is made, a new element - the function call and any arguments it is passed - is added on to the stack. The stack the computer uses to track function calls is referred to as the call stack.

# In contrast, problems solved using queues generally use an iterative solution involving a while loop.

# Although stack problems are often solved recursively, they may always be solved iteratively.

# Example Usage:

# Reverse a string using a iterative stack solution
def reverse_string_iterative(s):
    stack = []
    
    # Push all characters of the string onto the stack
    for char in s:
        stack.append(char)
    
    reversed_string = ""
    
    # Pop all characters from the stack and append to the result
    while stack:
        reversed_string += stack.pop()
    
    return reversed_string

# Reverse a string using a recursive stack solution
def reverse_string_recursive(s):
    # Base case: if the string is empty or has only one character
    if len(s) <= 1:
        return s
    
    # Recursive case: reverse the rest of the string and append the first character to the end
    # reverse_string_recursive(s[1:]) is added to call stack
    return reverse_string_recursive(s[1:]) + s[0]

# Sets
# Sets are a built-in data structure in Python that represent an unordered collection of unique elements. They are often used to track seen values, eliminate duplicates, and find overlap between multiple pieces of data.

# Sets maintain the following characteristics:

# Unordered: Sets do not maintain any particular order of elements (i.e. they are not indexed like lists or strings).
# Unique elements: Every element in a set must be unique. If a duplicate value is added to a set, the set will automatically remove the duplicate.
# Mutable: Sets can be modified. Values can be added or removed without needing to make a new set.
# Iterable: Sets can be iterated over using a loop
# A new set can be created using curly braces {} or using the set() function.

# Example Usage:

# Create a new Set
my_set = {1, 2, 3, 4}

# Using the set() function
another_set = set([1, 2, 3, 4])

# Creating an empty set
empty_set = set()  # Note: {} creates an empty dictionary, not a set
We can operate on a set using the following basic functions:

add(): Adds an element to the set.
remove(): Removes an element from the set. Raises a KeyError if the element is not found.
discard(): Removes an element if it is present, without raising an error if it is not found.
clear(): Removes all elements from the set.
Example Usage:

my_set = {1, 2, 3}

my_set.add(4)       # {1, 2, 3, 4}
my_set.remove(2)    # {1, 3, 4}
my_set.remove(5)    # Raises KeyError
my_set.discard(5)   # {1, 3, 4} - No error if element not found
my_set.clear()      # {}
Sets support various mathematical operations such as union, intersection, difference, and symmetric difference

# Union: a | b: Returns the set of elements contained in either set a or set b.
# Intersection: a & b: Returns the set of elements contained in both set a or set b.
# Difference: a - b: Returns the set of elements contained in set a but not in set b.
# Symmetric Difference: a ^ b: Returns the set of elements contained in either set a or set b but not in both.
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}

# Union: Elements in either set
union_set = set1 | set2           # {1, 2, 3, 4, 5}

# Intersection: Elements common to both sets
intersection_set = set1 & set2    # {3}

# Difference: Elements in set1 but not in set2
difference_set = set1 - set2      # {1, 2}

# Symmetric Difference: Elements in either set, but not both
symmetric_difference_set = set1 ^ set2  # {1, 2, 4, 5}