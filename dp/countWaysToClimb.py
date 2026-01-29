# Problem: There is a staircase with n steps. A person standing at the 
# 0-th step wants to reach the n-th one. They are capable of jumping up by 
# certain numbers of steps at a time. Given how the person can jump, 
# count the number of ways they can reach the top.


def count_ways_to_climb(steps, n):

    if n == 0 or n == 1:
        return n
    
    memo = [0] * (n+1)
    memo[0] = 0
    
    for i in range(1, n+1):
        for step in steps:
            if i - step >= 0:
                memo[i] += memo[i - step]
        if i in steps:
            memo[i] += 1
    
    return memo[n]

print(count_ways_to_climb([1, 2], 1)) #should be 2
print(count_ways_to_climb([1, 2], 2)) #should be 2
print(count_ways_to_climb([2, 3], 7)) #should be 3