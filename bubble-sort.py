# Bubble Sort Implementation
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr
    
print(bubble_sort([5, 8, 3, 9, 4, 1, 7]))