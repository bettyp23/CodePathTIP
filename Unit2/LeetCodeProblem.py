def create_dictionary(keys, values):
    return dict(zip(keys, values))

keys = ["peanut", "dragon", "star", "pop", "space"]
values = ["butter", "fly", "fish", "corn", "ship"]
result = create_dictionary(keys, values)
print(result)

def create_dict(keys, values):
    dictionary = {}
    for i in range(len(keys)):
        dictionary[keys[i]] = values[i]
    return dictionary

#----------------------------------------------

def print_pair(dictionary, target):
    if target in dictionary:
        print("Key: " + target)
        print("Value: " + dictionary[target])
    else:
        print("That pair does not exist")


dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")

#--------------------------------------------

def keys_v_values(dictionary):
    keySum = 0
    ValueSum = 0
    sum_of_keys = sum(dictionary.keys()) # can also use a loop
    
    # Calculate the sum of all values
    sum_of_values = sum(dictionary.values()) # can also use a loop
    
    # Determine which sum is greater or if they are equal
    if sum_of_keys > sum_of_values:
        return "keys"
    elif sum_of_values > sum_of_keys:
        return "values"
    else:
        return "balanced"

#----------------------------------------

dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
greater_sum = keys_v_values(dictionary1)
print(greater_sum)

dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
greater_sum = keys_v_values(dictionary2)
print(greater_sum)

#----------------------------------
