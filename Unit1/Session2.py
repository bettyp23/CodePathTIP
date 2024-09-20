#write print_list() that takes in a list lst as a parameter and prints out each item in the list.
lst = ["squirtle", "gengar", "charizard", "pikachu"]
def print_list(lst):
    for item in lst:
        print(item)

#print_list(lst)

#Write a function doubled() that takes in a list of integers lst as a parameter and prints each item in the list multiplied by two.

#def doubled(lst):
 #   for item in lst:
  #      print(2 * item) #print out double of each element

#Modify the function doubled() so that instead of printing the items, it returns a new list of the doubled numbers.

def doubled(lst):
    result = [] #empty list
    for num in lst:
        result.append(num*2) #adding a new value to the list
    return result

lst = [1,2,3]
new_lst= doubled(lst)
#print(lst)
#print(new_lst)

#Write a function flip_sign() that takes in a list of integers lst as a parameter and returns a new list where each number in the original list has been multiplied by -1.
def flip_sign(lst):
    new_lst = [] #empty list
    for num in lst:
        new_lst.append(num* -1)
    #print(new_lst)

lst2 = [1,2,3]
new_lst2= flip_sign(lst2)
#print(lst2)
#print(new_lst2)


#Write a function max_difference() that takes in a list of integers lst and returns the difference between the smallest and largest value in the list.
def max_difference(lst):
    max = lst[0] # start with the first element
    min = lst[0]

    for num in lst:
            if num > max:
                 max = num
            if num < min:
                min = num
        
    return max - min
        

lst3 = [5, 22, 8, 10, 2]
max_diff = max_difference(lst3)
#print(lst3)
#print(max_diff)


#Write a function count_less_than() that takes in a list of 
# integers numbers and an integer threshold as parameters and 
# returns the number of items in numbers that are less than threshold.

def count_less_than(numbers, threshold):
    counter = 0
    
    for num in numbers:
        if num < threshold:
            counter = counter + 1
    
    return counter

numbers = [12,8,2,4,4,10]
counter = count_less_than(numbers,5)
print(counter)


#Write a function get_evens() that takes in a list of integers 
#lst as a parameter and returns a list of all even numbers in the list.

def get_evens(lst):
    even_num = [] #empty list

    for num in lst:
        if (num%2 == 0):
             even_num.append(num)
    return even_num

#example
lst = [1,2,3,4,6]
evens_lst = get_evens(lst)
print(evens_lst)

#Write a function multiples_of_five() that prints 
# out multiples of 5 between 1 and 100 (inclusive).
def multiples_of_five():
    for num in range(1,100):
        if (num%5 == 0):
            print(num)

multiples_of_five()


#Write a function convertTemp() that takes in 
# celsius as a parameter, which denotes the 
# temperature in celsius.
def convertTemp(celsius):

    kelvin = celsius + 273.15
    fahrenheit = celsius * 1.80 + 32.00

    ans = [kelvin, fahrenheit]
    return ans

temperatures = convertTemp(23.00)
print(temperatures)