#Write a function is_monotonic() that takes in a list nums as a parameter 
# and checks if it is either monotone increasing or monotone decreasing.

def is_monotonic(nums):
    increasing = decreasing = True

    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            decreasing = False
        elif nums[i] < nums[i-1]:
            increasing = False

    return increasing or decreasing

nums1 = [1,2,2,3,10]
print(is_monotonic(nums1))

nums2 = [12,9,8,3,1]
print(is_monotonic(nums2))

nums3 = [1,1,1]
print(is_monotonic(nums3))

nums4 = [1,9,8,3,5]
print(is_monotonic(nums4))


#Write a function student_directory() that takes a list of student_names 
# as a parameter and returns a dictionary of students, where each student 
# in student_names is a key mapped to a unique numerical student ID.

def student_directory(student_names):
    student_dict = {}

    for i in range(len(student_names)):
        student_dict[student_names[i]] = i + 1
    return student_dict

student_names = ["Ada Lovelace", "Tu Youyou", "Mae Jemison", "Rajeshwari Chatterjee", "Alan Turing"]
print(student_directory(student_names))
