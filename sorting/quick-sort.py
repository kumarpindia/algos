# Quick Sort Algorithm Implementation in Python

# The quick sort algorithm is a popular sorting algorithm that uses the divide-and-conquer approach to
# sort elements in an array. It works by selecting a 'pivot' element from the array and partitioning the
# other elements into two sub-arrays, according to whether they are less than or greater than the pivot.
# The sub-arrays are then sorted recursively.

# The average and worst-case time complexity of quick sort is O(n log n), while the best-case time
# complexity is O(n). The space complexity of quick sort is O(log n) on average, but it can be O(n) in
# the worst case if the pivot selection is poor (e.g., when the smallest or largest element is always
# chosen as the pivot).

import random

def quick_sort(arr):
    
    helper(arr, 0, len(arr)-1)
    
    return arr
    

def helper(arr, start, end):
    
    #left node
    if start >= end:
        return
    
    smaller = start
    pivot = random.randint(start, end)
    arr[start], arr[pivot] = arr[pivot], arr[start]

    for bigger in range(start+1, end+1):
        if arr[bigger] < arr[start]:
            smaller += 1
            arr[smaller], arr[bigger] = arr[bigger], arr[smaller]
    
    arr[start], arr[smaller] = arr[smaller], arr[start]

    helper(arr, start, smaller-1)
    helper(arr, smaller+1, end)
    
    return arr


print(quick_sort([5, 8, 1, 3, 7, 9, 2])) #Output: [1, 2, 3, 5, 7, 8, 9]
print(quick_sort([5, 8, 3, 9, 4, 1, 7])) #Output: [1, 3, 4, 5, 7, 8, 9]
print(quick_sort([-913743, 3241, 999999, 1243153, 0, 0, 999999999])) #Output: [-913743, 0, 0, 3241, 1243153, 999999, 999999999]