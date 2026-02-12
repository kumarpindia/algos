# Given an array of integers and a target integer k, determine if it is possible to select a subset of
# the integers in the array that sum up to k. The subset can be empty, and the integers in the array can
# be positive, negative, or zero.

# Example 1:
# Input: arr = [2, 4, 8], k = 6
# Output: True
# Explanation: We can select the subset [2, 4] from the array, which sums up to 6. Therefore, it is
# possible to select a subset of the integers in the array that sum up to k, and the output is True. 

def check_if_sum_possible(arr, k):
    
    if k == 0 and sum(arr) == 0:
        return True
    
    result = [0]
    slate = []
    
    helper(arr, 0, k, slate, result)
    
    if result[0] > 0:
        return True
    else:
        return False


def helper(arr, i, k, slate, result):
    if i == len(arr):
        if len(slate) > 0 and sum(slate) == k:
            result[0] += 1
    else:
        helper(arr, i+1, k, slate, result)
        slate.append(arr[i])
        helper(arr, i+1, k, slate, result)
        slate.pop()


print(check_if_sum_possible([2, 4, 8], 6)) # Output: True
print(check_if_sum_possible([1], 0)) # Output: False