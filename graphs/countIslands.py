# Given a 2D grid of 1's (land) and 0's (water), count the number of islands. An island is surrounded by
# water and is formed by connecting adjacent lands horizontally, vertically, or diagonally. You may
# assume all four edges of the grid are all surrounded by water.
# Example 1:
# Input: grid = [
#   [1,1,0,0,0],
#   [0,1,0,0,1],
#   [1,0,0,1,1],
#   [0,0,0,0,0],
#   [1,0,1,0,1]
# ]
# Output: 5 
# Explanation: There are five islands in the grid. The first island is formed by the land in grid[0][0],
# grid[0][1], and grid[1][1]. The second island is formed by the land in grid[1][4]. The third island is
# formed by the land in grid[2][0]. The fourth island is formed by the land in grid[2][3] and grid[2][4].
# The fifth island is formed by the land in grid[4][0], grid[4][2], and grid[4][4].

ref_row = [-1, -1, -1, 0, 0, 1, 1, 1]
ref_col = [-1, 0, 1, -1, 1, -1, 0, 1]

def count_islands(matrix):
    
    islands = 0
    total_rows = len(matrix)
    total_cols = len(matrix[0])

    for row in range(total_rows):
        for col in range(total_cols):
            if matrix[row][col]:
                islands += 1
                dfs(row, col, matrix, total_rows, total_cols)

    return islands


def dfs(row, col, matrix, total_rows, total_cols):
    matrix[row][col] = 0
    for i in range(len(ref_row)):
        new_row = row + ref_row[i]
        new_col = col + ref_col[i]
        if new_row < 0 or new_row >= total_rows or new_col < 0 or new_col >= total_cols:
            continue
        if matrix[new_row][new_col] == 1:
            dfs(new_row, new_col, matrix, total_rows, total_cols)
        



print(count_islands([
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1]
    ]))