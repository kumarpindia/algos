# Implement the insertion sort algorithm to sort an array of integers in ascending order. The insertion
# sort algorithm builds the sorted array one element at a time by repeatedly taking the next unsorted
# element and inserting it into the correct position in the already sorted portion of the array.

# Example 1:
# Input: arr = [5, 2, 9, 1, 5, 6]
# Output: [1, 2, 5, 5, 6, 9]
# Explanation: The insertion sort algorithm sorts the array in ascending order by repeatedly taking the
# next unsorted element and inserting it into the correct position in the already sorted portion of
# the array. After sorting, the array becomes [1, 2, 5, 5, 6, 9].

def insertion_sort(arr):
    
    for i in range(len(arr)):
        temp = arr[i]
        j = i
        while j > 0 and temp < arr[j-1]:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = temp
        
    return arr

#print(insertion_sort([5, 2, 9, 1, 5, 6])) # Output: [1, 2, 5, 5, 6, 9]
#print(insertion_sort([5, 8, 3, 9, 4, 1, 7])) # Output: [1, 3, 4, 5, 7, 8, 9]
print(insertion_sort([-913743, 3241, 999999, 1243153, 0, 0, 999999999])) # Output: [-913743, 0, 0, 3241, 999999, 1243153, 999999999]