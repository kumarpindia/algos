# The number of ways to jump to the nth stair
# A person can jump either 1 stair or 2 stairs at a time.
# The number of ways to reach the nth stair can be defined as:# W(0) = 0
# W(1) = 1
# W(2) = 2
# W(n) = W(n-1) + W(n-2) for n > 2
# This implementation uses memoization to store previously computed values.
# Time Complexity: O(n)
# Space Complexity: O(n)
# Example:
# Input: n = 4
# Output: 5
# Explanation: The ways to reach the 4th stair are:# 1. 1+1+1+1
# 2. 1+1+2
# 3. 1+2+1
# 4. 2+1+1
# 5. 2+2

def jump_ways(n):
    
    if n == 0 or n == 1 or n == 2:
        return n
        
    ways = 0
    fib_arr = [-1] * (n+1)
    fib_arr[0] = 0
    fib_arr[1] = 1
    fib_arr[2] = 2
    
    for i in range(3, n+1):
        ways = fib(i, fib_arr)

    return ways
    

def fib(i, fib_arr):
    if fib_arr[i] != -1:
        return fib_arr[i]
    else:
        fib_arr[i] = fib(i-1, fib_arr) + fib(i-2, fib_arr)
        return fib_arr[i]
    


print(jump_ways(4))
print(jump_ways(3))
print(jump_ways(5))
print(jump_ways(0))