#Breakout Problems
#Write a function is_subsequence() that takes in a list 
# of integers lst and a list of integers sequence as parameters.
#Given these two lists, determine whether the sequence list 
# is a subsequence of the lst list. 

def is_subsequence(lst, sequence):
    seq_idx = 0
    for num in lst:
        if seq_idx == len(sequence):
            return True
        if sequence[seq_idx] == num:
            seq_idx += 1
    return False
    

lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(is_subsequence(lst, sequence))




#The function returns a dictionary where each item in keys is 
# paired with a corresponding item in values.

def create_dictionary(keys, values):
    result_dict = {}

    for i in range(len(keys)):
        result_dict[keys[i]] = values[i]
    return result_dict


keys = ["peanut", "dragon", "star", "pop", "space"]
values = ["butter", "fly", "fish", "corn", "ship"]
print(create_dictionary(keys, values))


#Write a function print_pair() 
# that takes in a dictionary dictionary 
# and a key target as parameters. The function looks for the target 
# and when found, it prints the key 
# and it's associated value as "Key: <key>" followed by 
# "Value: <value>". If target is not in dictionary, print 
# "That pair does not exist!".

def print_pair(dictionary, target):
    if target in dictionary:
        print("Key: " + target)
        print("Value: " + dictionary[target])
    else:
            print("That pair does not exist!")

dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")


#Write a function keys_v_values() that takes in a dictionary dictionary 
# whose keys and values are both integers. The function should find the 
# sum of all keys in the dictionary and the sum of all values.

def keys_v_values(dictionary):
    key_result = 0
    value_result = 0

    key_result = sum(dictionary.keys())

    for value in dictionary.values():
        value_result += value

    if key_result > value_result:
        return "keys"
    elif value_result > key_result:
        return "values"
    else:
        return "balanced"
    


dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
greater_sum = keys_v_values(dictionary1)
print(greater_sum)

dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
greater_sum = keys_v_values(dictionary2)
print(greater_sum)