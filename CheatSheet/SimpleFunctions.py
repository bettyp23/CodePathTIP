def hello_world(): # Function signature
	print("Hello world!") # Function body. Will print "Hello world!" to the console

hello_world() # Function call


#f-strings (using variables in strings)
first_name = 'albert'
last_name = 'einstein'
full_name = f"{first_name} {last_name}"
print(full_name)

#Dictionaries
#A simple dictionary
alien = {'color': 'green', 'points': 5}

#Accessing a value
print(f"The alien's color is {alien['color']}.")

#Adding a new key-value pair
alien['x_position'] = 0

#Looping through all key-value pairs
fav_numbers = {'eric': 7, 'ever': 4, 'erin': 47}
for name, number in fav_numbers.items():
 print(f"{name} loves {number}.")

#Looping through all keys
fav_numbers = {'eric': 7, 'ever': 4, 'erin': 47}
for name in fav_numbers.keys():
 print(f"{name} loves a number.")

#Looping through all the values
fav_numbers = {'eric': 7, 'ever': 4, 'erin': 47}
for number in fav_numbers.values():
 print(f"{number} is a favorite.")