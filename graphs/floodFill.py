# Given a 2D array representing an image, a starting pixel (pixel_row, pixel_column), and a new color,
# perform a flood fill on the image. A flood fill is a way of filling connected pixels with the same
# color as the starting pixel with a new color.

# Example 1:
# Input: pixel_row = 0, pixel_column = 1, new_color = 2, image = [[0, 1, 3], [1, 1, 1], [1, 5, 4]]
# Output: [[0, 2, 3], [2, 2, 2], [2, 5, 4]]
# Explanation: The starting pixel (0, 1) has the color 1. The connected pixels with the same color are
# (0, 1), (1, 0), (1, 1), and (1, 2). After performing the flood fill, these pixels are changed to the
# new color 2.

refs_row = [-1, 0, 1, 0]
refs_cols = [0, 1, 0, -1]

def flood_fill(pixel_row, pixel_column, new_color, image):

    # Check if the new color is the same as the old color in whole of image
    if any(x != new_color for row in image for x in row) == False:
        return image
    
    old_color = image[pixel_row][pixel_column]
    
    dfs(pixel_row, pixel_column, image, new_color, old_color)
                
    return image


def dfs(i, j, image, new_color, old_color):
    image[i][j] = new_color
    
    for k in range(len(refs_row)):
        new_row = refs_row[k] + i
        new_col = refs_cols[k] + j
        
        if new_row < 0 or new_row >= len(image) or new_col < 0 or new_col >= len(image[0]):
            continue
        
        if image[new_row][new_col] == old_color:
            dfs(new_row, new_col, image, new_color, old_color)



print(flood_fill(0, 1, 2, [
    [0, 1, 3],
    [1, 1, 1],
    [1, 5, 4]
    ])) # Output: [[0, 2, 3], [2, 2, 2], [2, 5, 4]]
print(flood_fill(1, 0, 9, [
    [0, 2, 1],
    [1, 1, 2],
    [2, 5, 4]
    ])) # Output: [[0, 2, 1], [9, 9, 2], [9, 5, 4]]
print(flood_fill(1, 1, 99, [
    [100, 100],
    [100, 100]
    ])) # Output: [[99, 99], [99, 99]]
print(flood_fill(0, 4, 7, [
    [7, 7, 7, 7, 7, 7],
    ])) # Output: [[7, 7, 7, 7, 7, 7]]