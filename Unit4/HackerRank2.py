"""

Write a function sort_list_by_parity() 
that takes in an integer list nums as a 
parameter and moves all the even integers 
at the beginning of the list followed by all 
the odd integers. The function returns any 
list that satisfies this condition.

"""

def sort_array_by_parity(nums):
    even = []
    odd = []

    for num in nums:
        if num % 2 == 0:
            even.append(num)
        if num % 2 != 0:
            odd.append(num)
    
    return even + odd

nums = [3,1,2,4]
nums2 = [0]
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))


"""
Write a function first_palindrome() 
that takes in a list of strings words 
as a parameter and returns the first 
palindromic string in the list. A string is 
palindromic if it reads the same forward and 
backward. If there is no such string, return an 
empty string
"""

def first_palindrome(words):
    for word in words:
        if word == word[::-1]:
            return word
    return ""



words = ["abc","car","ada","racecar","cool"]
palindrome1 = first_palindrome(words)
print(palindrome1)

words2 = ["abc","racecar","cool"]
palindrome2 = first_palindrome(words2)
print(palindrome2)

words3 = ["abc", "def", "ghi"]
palindrome3 = first_palindrome(words3)
print(palindrome3)


"""
Write a function remove_duplicates() 
that takes in a sorted list of integers 
nums as a parameter and removes the duplicates 
in-place such that each element appears only once. 
Do not allocate extra space for another array; you 
must do this by modifying the input list with O(1) 
extra memory. The function returns the new length of the list.
"""

def remove_duplicates(nums):

    if not nums:
        return 0

    # Pointer for the position of the next unique element
    unique_pos = 0

    # Iterate through the list starting from the second element
    for i in range(1, len(nums)):
        # If the current element is different from the element at unique_pos, it's a unique element
        if nums[i] != nums[unique_pos]:
            unique_pos += 1
            nums[unique_pos] = nums[i]

    # The list is modified in place. We need to truncate the list to the new length.
    # Trim the list to contain only the unique elements.
    del nums[unique_pos + 1:]

    # Return the length of the list after removing duplicates
    return unique_pos + 1

nums = [1,1,2,3,4,4,4,5]
print(nums)
print(remove_duplicates(nums))
print(nums) # same list


"""
Write a function is_perfect_number() that takes in a positive 
integer n and returns True if it is a perfect number and False 
otherwise. A perfect number is a positive integer that is equal 
to the sum of its proper divisors, excluding itself.

For example, 6 is a perfect number because its divisors or 1, 2, and 3 and 1 + 2 + 3 = 6.
"""

def is_perfect_number(n):
    
    if n<=1:
        return False

    sum = 0
    for count in range(1, n //2 + 1): #yeilds floating point
        if n % count == 0:
            sum += count

    return sum == n
        

print(is_perfect_number(6))
print(is_perfect_number(28))
print(is_perfect_number(9),"\n")




"""
Twwo pointer approach
Write a function is_palindrome() that 
takes in a string s as a parameter and 
returns True if the string is a palindrome 
and False otherwise. You may assume the 
string contains only lowercase alphabetic characters.
"""

def is_palindrome(s):
    left = 0
    right = len(s)-1

    while left < right:
        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True

s = "amanaplanacanalpanama"
s2 = "helloworld"

print(is_palindrome(s))
print(is_palindrome(s2))



"""
Write a function reverse_vowel() 
that takes in a string s as a 
parameter and returns a string 
with all the vowels in the string 
reversed. The consonants should 
remain in the same position. For 
this question, we consider a, e, i, o, and u 
as vowels but not y. The vowels can appear 
in both lower and upper cases, more than once.
"""

def reverse_vowels(s):
    vowels = "aeiouAEIOU"  # Consider both lowercase and uppercase vowels
    vowel_indices = []  # List to store the indices of the vowels in the string
    vowel_chars = []    # List to store the vowel characters

    # Collect indices and characters of the vowels
    for index, char in enumerate(s):
        if char in vowels:
            vowel_indices.append(index)    # Save the index of the vowel
            vowel_chars.append(char)        # Save the vowel character

    # Reverse the list of vowels
    vowel_chars.reverse()

    # Convert the string to a list to allow modification
    s_list = list(s)

    # Place the reversed vowels back into their original positions
    for i, index in enumerate(vowel_indices):
        s_list[index] = vowel_chars[i]

    # Convert the list back to a string and return it
    return ''.join(s_list)

# Example usage
s1 = "hello"
rev_s1 = reverse_vowels(s1)
print(rev_s1)  # Output: holle

s2 = "leetcode"
rev_s2 = reverse_vowels(s2)
print(rev_s2)  # Output: leotcede



"""
Write a function removeElement() 
that takes in a list nums and a 
value val as parameters and removes 
all instances of that value in-place. 
The function returns the new length of nums.
"""

def removeElement(nums, val):
    # Create a new list with elements that are not equal to val
    nums[:] = [num for num in nums if num != val]  # This modifies the original list in place
    return len(nums)  # Return the new length of the list

nums = [5, 4, 4, 3, 4, 1]
nums_len = removeElement(nums, 4)
print(nums)      # Output: [5, 3, 1] (the modified list)
print(nums_len)  # Output: 3 (the length of the modified list)
