# Python3 program to find nCr using Dynamic Programming (Memoization)
# The binomial coefficient nCr is defined as:
# nCr = n! / (r! * (n-r)!)
# It can also be defined using the following recursive relation:
# nCr = n-1Cr + n-1Cr-1
# with base cases:
# nC0 = 1
# nCn = 1
# This implementation uses memoization to store previously computed values.
# Time Complexity: O(n*r)
# Space Complexity: O(n*r)
# Example:
# Input: n = 5, r = 3
# Output: 10

P = 1000000007

def ncr(n, r):

    fib_arr = [[-1 for _ in range(r+1)] for _ in range(n+1)]

    return find_num(n, r, fib_arr)
    

def find_num(n, r, fib_arr):
    if r > n:
        return 0
    if r == n or r == 0:
        return 1
        
    if fib_arr[n][r] != -1:
        return fib_arr[n][r]
    else:
        fib_arr[n][r] = (find_num(n-1, r, fib_arr) + find_num(n-1, r-1, fib_arr)) % P
        return fib_arr[n][r]
    


print(ncr(5, 3)) #should be 10
print(ncr(8, 3)) #should be 56