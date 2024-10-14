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

#Slice the string and then swipe the values

def swap_ends(my_str):
    # print(my_str[-1])
    # print(my_str[-1:]) #slices are better bc of possible index errors
    return my_str[-1] + my_str[1:-1] + my_str[0]
  

my_str = "mystring"
swapped = swap_ends(my_str)
print(swapped)


"""
A pangram is a sentence containing every letter in the English alphabet.
"""

#create string with every letter in alphabet
#if str does not have a letter in new string return false : true
def is_pangram(Str):
    alph = "abcdefghijklmnopqrstuv"

    for char in alph:
        if char not in Str.lower():
            return False
        return True

my_str = "The quick brown fox jumps over the lazy dog"
print(is_pangram(my_str))

str2 = "The dog jumped"
print(is_pangram(str2))


"""
Write a function first_unique_char() 
that given a string my_str as a parameter, 
it finds the first non-repeating character 
in it and returns its index. If it does not 
exist, then return -1.

"""

#counter of how many we see this character
#for every character in  string, check if it repeats
#

def first_unique_char(myStr):
    # Count occurrences
    char_count = {}
    for char in myStr:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Find the first non-repeating character
    # enumerate gets both the index and the value of each element.
    #index is the current positions
    for index, char in enumerate(myStr):
        if char_count[char] == 1:
            return index
    return -1
    

my_str = "leetcode"
print(first_unique_char(my_str))

str2 = "loveleetcode"
print(first_unique_char(str2))

str3 = "aabb"
print(first_unique_char(str3))



"""
Write a function remove_char() that 
takes in a string s and an integer n as 
parameters, The function returns a new string 
with the nth character removed where 0 < n < len(s).
"""

def remove_char(s, n):
    first = s[:n]
    last = s[n+1:]

    return first + last

s = "typpo"
fixed_s = remove_char(s, 2)
print(fixed_s)




"""
Write a function vowel_count() that takes 
in a string s as a parameter and returns the 
number of vowels in the given string.
"""
def vowel_count(s):
    vowel = "aeiou"
    count = 0

    for char in s:
        if char.lower() in vowel:
            count += 1
    return count


my_str = "hello world"
my_str2 = "aAaAaAaAAA"
my_str3 = "ths strng s mssng vwls"

count1 = vowel_count(my_str)
print(count1)
count2 = vowel_count(my_str2)
print(count2)
count3 = vowel_count(my_str3)
print(count3)



"""
Write a function reverse_sentence() that 
takes in a string sentence as a parameter and 
returns the string with the sentence but with 
the order of the words reversed. The sentence will 
only contain alphabetic characters and spaces to separate 
the words. If there is only one word in the sentence, the 
function returns the original string.
"""

def reverse_sentence(sentence):
    words = sentence.split(' ')
    reversed_words = words[::-1]
    reversed_sentence= ' '.join(reversed_words)
    return reversed_sentence

sentence = "I solemnly swear I am up to no good"
print(reverse_sentence(sentence))


"""
the string "aabcccccaaa" would become "a2b1c5a3"
"""


def compress_string(myStr):
    if not myStr:
        return ""
    result = ""
    count = 1
    current_char = myStr[0]
    for i in range(1, len(myStr)):
        if myStr[i] == current_char:
            count += 1
        else:
            result += current_char + str(count)
            current_char = myStr[i]
            count = 1
    result += current_char + str(count)
    if len(result) < len(myStr):
        return result
    else:
        return myStr

my_str = "aaaaabbcccd"
compressed_Str = compress_string(my_str)
print(compressed_Str)

my_str2 = "abcde"
compressed_Str2 = compress_string(my_str2)
print(compressed_Str2)