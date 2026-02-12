# Given a 2D grid of 0s and 1s, find the size of the largest island of 1s. An island is a group of
# adjacent 1s connected horizontally or vertically (not diagonally). The size of an island is the number
# of cells with value 1 in that island.

# Example 1:
# Input: grid = [[1, 1, 0], [1, 1, 0], [0, 0, 1]] 
# Output: 4
# Explanation: The largest island of 1s has a size of 4, which is formed by the 1s in the top-left
# corner of the grid. The island consists of the cells (0, 0), (0, 1), (1, 0), and (1, 1). 
# The cell (2, 2) is a separate island of size 1, which is smaller than the largest island.

refs_row = [-1, 0, 1, 0]
refs_col = [0, 1, 0, -1]

def max_island_size(grid):
    answer = island_size = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                island_size = dfs(i, j, grid)
                answer = max(answer, island_size)

    return answer
                
                
def dfs(row, col, grid):
    grid[row][col] = -1
    count = 1
    
    for k in range(len(refs_row)):
        new_row = refs_row[k] + row
        new_col = refs_col[k] + col
        
        if new_row < 0 or new_row >= len(grid) or new_col < 0 or new_col >= len(grid[0]):
            continue
        
        if grid[new_row][new_col] == 1:
            count += dfs(new_row, new_col, grid)

    return count    



print(max_island_size([
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
    ])) # Output: 4
print(max_island_size([
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
    ])) # Output: 0