#Write a function find_minimum(list) that returns the smallest element in the list

#UMPIRE: understand
#1. Questions: is the list empty, will it be null, how big, is the list sorted
#2. Basic sample input / output: [x, z, l, a] then the output should be a. none is python version of null
#3. edge cases. empty lists, varients: characters can be compared

#UMPIRE: plan
#1. Approach: going to go through the list and find the smallest element, then return
#2. English steps: 
    #if list is empty, we return none
    #Create a current n variable to hold the smallest element
    #Go through the list for each element ->
        #if element is smaller than current_min
        #set current_min to the element
    #return current_min

#UMPIRE: implement
def find_minimum(lst):

    if not lst:                         #checks if the list is empty
        return None
    
    current_min = lst[0]                #initialize current_min with the first element

    for element in lst[1:]:             #look through the list staring from the second element
        if element < current_min:       #if element is smaller, update current_min
            current_min = element

    return current_min                  #Return the smallest element found