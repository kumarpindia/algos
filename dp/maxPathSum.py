# Problem: Given a two dimensional grid of numbers. Find a path from top-left corner to bottom-right
# corner, which maximizes the sum of all numbers along its path. You can only move either down or 
# right from your current position.

def maximum_path_sum(grid):
    
    rows_count = len(grid)
    cols_count = len(grid[0])

    memo = [[-1 for _ in range(cols_count+1)] for _ in range(rows_count+1)]
    
    return find_path(rows_count-1, cols_count-1, grid, memo)
    

def find_path(row, col, grid, memo):
    if row == 0 and col == 0:
        return grid[0][0]
    if memo[row][col] != -1:
        return memo[row][col]
    else:
        if row == 0:
            memo[row][col] = find_path(row, col-1, grid, memo) + grid[row][col]
        elif col == 0:
            memo[row][col] = find_path(row-1, col, grid, memo) + grid[row][col]
        else:
            memo[row][col] = max(find_path(row, col-1, grid, memo), find_path(row-1, col, grid, memo)) + grid[row][col]
        
        return memo[row][col]

    

print(maximum_path_sum([ 
    [4, 5, 8],
    [3, 6, 4],
    [2, 4, 7]
    ])) #should be 28