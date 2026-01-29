#Problem: Find unique paths in a grid from top-left to bottom-right

mod = 10**9 + 7 

def unique_paths(n, m):

    dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]
    
    return find_paths_count(n, m, dp)
    
    
def find_paths_count(row, col, dp):
    if row == 1 or col == 1:
        return 1
    if dp[row][col] != -1:
        return dp[row][col]
    else:
        dp[row][col] = (find_paths_count(row-1, col, dp) + find_paths_count(row, col-1, dp)) % mod
        return dp[row][col]
    

print(unique_paths(3, 2)) #should be 3
print(unique_paths(5, 5)) #should be 70