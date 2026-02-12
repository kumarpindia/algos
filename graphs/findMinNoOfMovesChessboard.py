# Given a chessboard of size rows x cols, find the minimum number of moves required for a knight to move
# from a starting position (start_row, start_col) to an ending position (end_row, end_col). The knight
# moves in an "L" shape: two squares in one direction and then one square perpendicular to that.

# Example 1:
# Input: rows = 5, cols = 5, start_row = 0, start_col = 0, end_row = 4, end_col = 1
# Output: 3
# Explanation: The knight can move from (0, 0) to (2, 1) to (4, 0) to (4, 1). Therefore, the minimum
# number of moves required is 3.

refs_row = [-2, -2, -1, 1, 2, 2, 1, -1]
refs_col = [-1, 1, 2, 2, 1, -1, -2, -2]

def find_minimum_number_of_moves(rows, cols, start_row, start_col, end_row, end_col):
    
    if start_row == end_row and start_col == end_col:
        return 0
    
    board = [[0 for _ in range(cols)] for _ in range(rows)]
    
    q = []
    q.append((start_row, start_col))  # (row, col)

    while q:
        current = q.pop(0)
        i = current[0]
        j = current[1]

        for k in range(len(refs_row)):
            new_row = refs_row[k] + i
            new_col = refs_col[k] + j
        
            if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
                continue
            if board[new_row][new_col] == 0:
                board[new_row][new_col] = board[i][j] + 1
                if new_row == end_row and new_col == end_col:
                    return board[new_row][new_col]
                q.append((new_row, new_col))

    return -1
    

print(find_minimum_number_of_moves(5, 5, 0, 0, 4, 1)) # Output: 3
print(find_minimum_number_of_moves(1, 1, 0, 0, 0, 0)) # Output: 0
