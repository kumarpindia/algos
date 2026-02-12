# Given a matrix of integers, find the sizes of the basins in the matrix. A basin is defined as a group
# of connected cells (connected horizontally or vertically) that all flow to the same local minimum.
# A local minimum is a cell that has a value less than all of its neighbors (up, down, left, right). 
# The size of a basin is the number of cells in it.

# The function first initializes a 2D list to keep track of the basin index for each cell, and a 
# variable to keep track of the current basin index. It then iterates through each cell in the input 
# matrix, performing a depth-first search (DFS) to find the local minimum that the cell flows to. If the
# local minimum is found and has not been assigned a basin index yet, it assigns the current basin index
# to all cells that flow to that local minimum. Finally, it counts the size of each basin and sorts the
# sizes using counting sort before returning the sorted list of basin sizes.

# Time complexity: O(m*n) where m is the number of rows and n is the number of columns in the input
# matrix, due to the need to visit each cell at least once and potentially perform a DFS for each cell.
# The counting sort step has a time complexity of O(k) where k is the range of basin sizes, which is
# typically much smaller than m*n.

def find_basins(matrix):
    rows_count = len(matrix)
    cols_count = len(matrix[0])
    
    basins = [[-1] * cols_count for _ in range(rows_count)]
    basin_index = 0
    
    for i in range(rows_count):
        for j in range(cols_count):
            if dfs(i, j, basins, matrix, basin_index) == basin_index:
                basin_index += 1
    
    basin_sizes = [0] * basin_index

    for i in range(rows_count):
        for j in range(cols_count):
            basin_sizes[basins[i][j]] += 1

    count_sort(basin_sizes)

    return basin_sizes
    

def count_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    range_val = max_val - min_val + 1

    count = [0] * range_val
    output = [0] * len(arr)

    for i in range(len(arr)):
        count[arr[i] - min_val] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1
    for i in range(len(arr)):
        arr[i] = output[i]


def dfs(row, col, basins, matrix, basins_index):
    if basins[row][col] == -1:
        min_row, min_col = row, col

        if row > 0 and matrix[row - 1][col] < matrix[min_row][min_col]:
            min_row = row - 1
            min_col = col
        if col < len(matrix[0]) - 1 and matrix[row][col + 1] < matrix[min_row][min_col]:
            min_row = row
            min_col = col + 1
        if row < len(matrix) - 1 and matrix[row + 1][col] < matrix[min_row][min_col]:
            min_row = row + 1
            min_col = col
        if col > 0 and matrix[row][col - 1] < matrix[min_row][min_col]:
            min_row = row
            min_col = col - 1
        
        if min_row == row and min_col == col:
            basins[row][col] = basins_index
        else:
            basins[row][col] = dfs(min_row, min_col, basins, matrix, basins_index)
        
    return basins[row][col]



print(find_basins([
    [1, 5, 2],
    [2, 4, 7],
    [3, 6, 9]
]))  # [2, 7] expected output
