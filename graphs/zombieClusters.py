# A group of zombies is called a cluster. A cluster is defined as a group of adjacent zombies. Two 
# zombies are adjacent if they are next to each other horizontally or vertically (not diagonally). 
# Given a map of zombies in the form of an array of strings, where each string represents a row and 
# each character in the string represents a cell that can either be '0' (empty) or '1' (zombie), write 
# a function that returns the number of zombie clusters.

# The function first converts the input array of strings into a 2D matrix of integers for easier 
# manipulation. It then iterates through each cell in the matrix, and whenever it encounters a '1' 
# (indicating a zombie), it increments the cluster count and performs a depth-first search (DFS) to mark
# all adjacent zombies as visited (by changing their value to -1). This ensures that each cluster is 
# counted only once. Finally, the function returns the total number of clusters found.

# Time complexity: O(m*n) where m is the number of rows and n is the number of columns in the input 
# matrix, due to the need to visit each cell at least once and potentially perform a DFS for each 
# cluster found.

ref_rows = [-1, 0, 1, 0]
ref_cols = [0, 1, 0, -1]

def zombie_cluster(zombies):
    matrix = []
    cluster = 0
    
    for row in zombies:
        matrix.append([int(c) for c in row])
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                cluster += 1
                dfs(i, j, matrix)
    
    return cluster

def dfs(row, col, matrix):
    matrix[row][col] = -1
    
    for i in range(len(ref_rows)):
        new_row = ref_rows[i] + row
        new_col = ref_cols[i] + col
        
        if new_row < 0 or new_row >= len(matrix) or new_col < 0 or new_col >= len(matrix[0]):
            continue
        
        if matrix[new_row][new_col] == 1:
            dfs(new_row, new_col, matrix)
        


print(zombie_cluster(["1100", "1110", "0110", "0001"])) #expected output 2