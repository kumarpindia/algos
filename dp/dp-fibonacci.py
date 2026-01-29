# Fibonacci using Dynamic Programming (Memoization)
# The Fibonacci sequence is defined as:
# F(0) = 0
# F(1) = 1
# F(n) = F(n-1) + F(n-2) for n >
# 1
# This implementation uses memoization to store previously computed Fibonacci numbers.
# Time Complexity: O(n)
# Space Complexity: O(n)
# Example:
# Input: n = 10
# Output: 55
# Explanation: The 10th Fibonacci number is 55.

def find_fibonacci(n):
    if n == 0 or n == 1:
        return n

    fib_arr = [-1] * (n+1)
    fib_arr[0] = 0
    fib_arr[1] = 1
    
    return find_fib(n, fib_arr)
    

def find_fib(n, fib_arr):
    if fib_arr[n] >= 0:
        return fib_arr[n]
    else:
        sum = find_fib(n-1, fib_arr) + find_fib(n-2, fib_arr)
        fib_arr[n] = sum
        return sum
    


print(find_fibonacci(10))
print(find_fibonacci(0))