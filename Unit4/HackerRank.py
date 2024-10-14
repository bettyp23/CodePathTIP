def mystery_function(key, value, dict):
    if key in dict:
        dict[key].append(value)
    else:
        dict[key] = [value]
    return dict

dict = {'a': [1,2]}
output = mystery_function('c', 5, dict)
print(output)


############################


def get_patients(doctor, patients):
    names = []

    for patient, patient_doctor in patient.items():
        if patient_doctor == doctor:
            names.append(patient)

    return names


doctor = "Dr. Banner"
patients = {"Jane Doe": "Dr.Banner"}
##output = [Jane Doe]


##################################

def find_unique(nums):
    counts = {}

    for num in nums:
        if num in counts:
            counts[num] + 1
        else:
            counts[num] = 1

    for num in counts:
        if counts[num] == 1:
            return num
        

        
    