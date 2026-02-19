# Given an integer n, find the number of structurally unique binary search trees (BSTs) that can be
# formed with values from 1 to n.

# Example 1:
# Input: n = 3
# Output: 5
# Explanation: There are 5 unique BSTs that can be formed with values from 1 to 3:
# 1.   1         2.   1         3.   2         4.   3         5.   2            3            1            1            2
#      \              \              \              \              \
#       3               2              3              1              3

def how_many_bsts(n):
    ans = 0
    
    if n == 0 or n == 1:
        return 1
    else:
        for i in range(1, n+1):
            ans += how_many_bsts(i-1) * how_many_bsts(n-i)
    
    return ans
    

print(how_many_bsts(3)) # Output: 5