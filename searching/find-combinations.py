# Combination Finder
# Description: This script finds all possible combinations of k numbers
# chosen from the range 1 to n. It uses a backtracking approach to explore
# all possible combinations and stores the results in a list.

# For example, given n = 5 and k = 2, the output will be: [[1, 2], [1, 3], [1, 4], 
# [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]].

# Time Complexity: O(C(n, k)) where C(n, k) is the number of combinations.
# Space Complexity: O(k) for the recursion stack and O(C(n, k)) for storing the results.

def find_combinations(n, k):
    
    arr = []
    
    def backtrack(start, path):
        if len(path) == k:
            arr.append(path[:]) 
            return
        for i in range(start, n+1):
            path.append(i)
            backtrack(i+1, path)
            path.pop()
    
    backtrack(1, [])
    return arr

print(find_combinations(5, 2)) #should be [[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]]
print(find_combinations(6, 6)) #should be [[1, 2, 3, 4, 5, 6]]