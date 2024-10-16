10/15/24

Python classes

Class encapsulate data for the object and methods to manipulate that data

Instantiation - > creating an instance (object) of a class


A set in Python is a collection of unique elements, meaning it does not allow duplicates. Sets are unordered, so the elements do not have a specific order. Sets are mutable, meaning you can add or remove elements, but each element must be immutable (e.g., numbers, strings, tuples).

Example of a Set:
python
Copy code
# Creating a set
my_set = {1, 2, 3, 4, 4}
print(my_set)  # Output: {1, 2, 3, 4}

# Checking if an element exists in a set
print(2 in my_set)  # Output: True
In this example:

Duplicates (like 4 in the set) are automatically removed.
add() is used to add elements, and remove() is used to remove elements.
Sets are useful when you need to maintain a collection of unique items.




self - > an instance of this class
first parameter of class, python will pass self
self.(something) inside the class code


