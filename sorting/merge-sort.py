# Given an array of integers, sort the array in ascending order using the merge sort algorithm.
# Example:
# Input: arr = [5, 8, 3, 9, 4, 1, 7]
# Output: [1, 3, 4, 5, 7, 8, 9] 
# Explanation: The sorted array is [1, 3, 4, 5, 7, 8, 9]. 

def merge_sort(arr):
    
    helper(arr, 0, len(arr)-1)
    
    return arr

def helper(arr, start, end):
    
    if start >= end:
        return
    
    mid = (start + end) // 2
    
    helper(arr, start, mid)
    helper(arr, mid+1, end)
    
    aux_arr = []
    i = start
    j = mid + 1
    
    while i<=mid and j<=end:
        if arr[i] <= arr[j]:
            aux_arr.append(arr[i])
            i += 1
        else:
            aux_arr.append(arr[j])
            j += 1

    while i <= mid:
        aux_arr.append(arr[i])
        i += 1
        
    while j <= end:
        aux_arr.append(arr[j])
        j += 1
    
    for k in range(len(aux_arr)):
        arr[start + k] = aux_arr[k]

    return arr

print(merge_sort([-913743, 3241, 999999, 1243153, 0, 0, 999999999])) # Output: [-913743, 0, 3241, 999999, 1243153, 999999999]
print(merge_sort([5, 8, 3, 9, 4, 1, 7])) # Output: [1, 3, 4, 5, 7, 8, 9]
print(merge_sort([12, 11, 13, 5, 6, 7])) # Output: [5, 6, 7, 11, 12, 13]
print(merge_sort([12, 11, 13])) # Output: [11, 12, 13]
print(merge_sort([12, 11, 13, 5])) # Output: [5, 11, 12, 13]
print(merge_sort([12, 11])) # Output: [11, 12]