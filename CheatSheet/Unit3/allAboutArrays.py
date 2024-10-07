#Arrays can be implemented using built-in list data type or using the array
#module from the standard library

#list preferred as they are more versatile

#creating an array
arr = [1,2,3,4,5]

#Access elements
print(arr[0]) #outputs 1
print(arr[-1]) #outputs 5 (last element)

#modify elemnts
arr[2] = 10 #array is now [1, 2, 10, 4, 5]

#append = add elements
arr.append(6)   #array becomes [1, 2, 10, 4, 5, 6]

#insert elements at specific index
arr.insert(2,3) #array becomes [1, 2, 3, 10, 4, 5, 6]

#remove elements
arr.pop()   #removes last element 
arr.remove(10) #removes the first occurance of 10

#length of array
print(len(arr)) #output: 6 (after previous modifications)

#---------------------------------------------------------------

#Slicing arrays

arr = [1, 2, 3, 4, 5]

print(arr[1:4]) #output: [2,3,4] (slice from index 1 to 3)
print(arr[:2]) #ouput: [1,2] (slice from start to index 1)
print(arr[2:]) #output [3, 4, 5] (slice from index 2 to end)
 


#common functions find minimum, maximum, and sum
print(min(arr))
print(max(arr))
print(sum(arr))

#sort an array
arr.sort()  #sorts ascending order

#reverse
arr.reverse()   #reverses the array in-place

#iteration
for num in arr:
    print(num)