# Dutch National Flag problem: Sort an array of balls represented by "R", "G", and "B"
# "R" for Red, "G" for Green, and "B" for Blue.
# The goal is to sort the balls in the order of Red, Green, and Blue.
# Time Complexity: O(n)
# Space Complexity: O(1)
# We will use three pointers to partition the array into three sections.
# low for "R", mid for "G", and high for "B".
# We will iterate through the array and swap elements to their correct positions.
# When mid pointer encounters "R", we swap it with the low pointer and increment both.
# When mid pointer encounters "G", we just increment mid pointer.
# When mid pointer encounters "B", we swap it with the high pointer and decrement high pointer
# without incrementing mid pointer.
 
def dutch_flag_sort(balls):
    
    low, mid, high = 0, 0, len(balls)-1

    while mid <= high:
        if balls[mid] == "R":
            balls[low], balls[mid] = balls[mid], balls[low]
            low += 1
            mid += 1
        elif balls[mid] == "G":
            mid += 1
        else:
            balls[mid], balls[high] = balls[high], balls[mid]
            high -= 1
    
    return balls


print(dutch_flag_sort(["G", "B", "R", "R", "B", "R", "G"]))