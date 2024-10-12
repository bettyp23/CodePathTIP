#Write a function is_prime() that takes in a positive 
# integer n and returns True if it is a prime number 
# and False otherwise. A prime number is a number 
# greater than 1 that has no positive divisors other 
# than 1 and itself.

def is_prime(n):
    x  = 2

    while x < n-1:
        if n % x == 0:
            return False
        x += 1
        
    return True

print(is_prime(5))
print(is_prime(12))
print(is_prime(15))

"""
Write function reverse_list()
return elements of list in reversed order
not allowed to use list slicing (lst[::-1])
"""


def reverse_list(lst):
    start = 0
    end = len(lst) -1 

    while (start != end or start < end):
        lst[start], lst[end] = lst[end], lst [start]

        start += 1
        end -= 1
    return lst 


lst =  [ 1, 2, 3, 4, 5 ]
print(reverse_list(lst))




"""
make up practice
"""

def index_to_value_map(lst):
    index = {}

    for item in lst:
        lst.append()
        print(index)

lst = ["apple", "banana", "cherry"]

#print(index_to_value_map(lst))