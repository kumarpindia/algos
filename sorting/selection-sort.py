# This function implements the selection sort algorithm to sort a list of integers in ascending order.
# The selection sort algorithm works by repeatedly selecting the smallest unsorted element and swapping it with
# the first unsorted element until the entire list is sorted.

# For example, given the input [5, 8, 3, 9, 4, 1, 7], the output would be [1, 3, 4, 5, 7, 8, 9].# The function
# should return the sorted list.

# Note: The function should modify the input list in place and return it.

def selection_sort(arr):
    
    min_val_index = 0
    
    for i in range(len(arr)):
        min_val_index = i+1
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i] and arr[j] <= arr[min_val_index]:
                min_val_index = j
                arr[i], arr[min_val_index] = arr[min_val_index], arr[i]
    return arr
    
print(selection_sort([5, 8, 3, 9, 4, 1, 7]))
print(selection_sort([-913743, 3241, 999999, 1243153, 0, 0, 999999999]))