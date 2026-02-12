# Given two sorted arrays, merge the first array into the second one. The second array has enough space
# to hold all the elements of the first array, and the number of elements initialized in the second array
# is equal to the number of elements in the first array.
# Example:
# Input: first = [1, 3, 5], second = [2, 4, 6, 0, 0, 0]
# Output: [1, 2, 3, 4, 5, 6]

def merge_one_into_another(first, second):
    
    i = 0
    j = 0   
    aux_arr = []
    
    while i < len(first) and j < len(second) and second[j] != 0:
        if first[i] <= second[j]:
            aux_arr.append(first[i])
            i += 1
        else:
            aux_arr.append(second[j])
            j += 1
    
    while i < len(first):
        aux_arr.append(first[i])
        i += 1
    
    while j < len(second) and second[j] != 0:
        aux_arr.append(second[j])
        j += 1
        
    for k in range(len(aux_arr)):
        second[k] = aux_arr[k]
    
    return second

print(merge_one_into_another([1, 3, 5], [2, 4, 6, 0, 0, 0])) # Output: [1, 2, 3, 4, 5, 6]
print(merge_one_into_another([-913743, 3241, 999999, 1243153, 999999999], [5, 8, 9, 0, 0, 0, 0, 0])) # Output: [-913743, 5, 8, 9, 3241, 999999, 1243153, 999999999]
print(merge_one_into_another([12, 13], [5, 6, 7, 0, 0])) # Output: [5, 6, 7, 12, 13]