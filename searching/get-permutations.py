# Given an array of distinct integers, return all possible permutations. You can return the answer in 
# any order.
# For example, given the array [1,2,3], the permutations would be: [1,2,3], [1,3,2], [2,1,3], [2,3,1], 
# [3,1,2], [3,2,1].

# The function uses a helper function to recursively build the permutations by selecting each element 
# and generating permutations of the remaining elements. The main function initializes the necessary
# variables and calls the helper function, which performs the actual permutation generation. The
# results are returned as a list of permutations.
# Example usage is provided at the end, where the function is called with the array [1,2,3] to generate 
# its permutations.

# Time complexity: O(n * n!) where n is the length of the input array, due to the recursive nature of 
# the permutation generation and the fact that there are n! permutations of n distinct integers.

def get_permutations(arr):
    
    result = []
    slate = []
    phelper(slate, result, arr)
    return result


def phelper(slate, result, arr):
    if (len(arr) == 0):
        result.append(slate)
    else:
        for i in range(len(arr)):
            phelper(slate + [arr[i]], result, arr[:i] + arr[i+1:])


print(get_permutations([1,2,3]))