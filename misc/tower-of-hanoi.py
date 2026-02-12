# This function solves the Tower of Hanoi problem for n disks. The function returns a list of moves required to
# move n disks from the source peg to the destination peg using an auxiliary peg.
# The Tower of Hanoi is a mathematical puzzle where you have three pegs and n disks of different sizes which
# can slide onto any peg. The puzzle starts with the disks in a neat stack in ascending order of size on one
# peg, the smallest at the top, thus making a conical shape. The objective of the puzzle is to move the entire
# stack to another peg, following these simple rules:
# 1. Only one disk can be moved at a time.
# 2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack
# or on an empty peg.
# 3. No disk may be placed on top of a smaller disk.

# For example, if n = 2, the output would be [[1, 2], [1, 3], [2, 3]], which represents the moves required to
# move 2 disks from peg 1 to peg 3 using peg 2 as an auxiliary peg.
# The function should return a list of moves, where each move is represented as a list of two integers [from_
# peg, to_peg], indicating the peg from which a disk is moved and the peg to which it is moved.
# For example, if n = 3, the output would be [[1, 3], [1, 2], [3, 2], [1, 3], [2, 1], [2, 3], [1, 3]], which
# represents the moves required to move 3 disks from peg 1 to peg 3 using peg 2 as an auxiliary peg.
# Note: The function should return the moves in the order they are performed.
 
def tower_of_hanoi(n):

    result = []
    helper(n, 1, 2, 3, result)

    return result


def helper(n, src, aux, dest, result):
    if n == 1:
        result.append([src, dest])
    else:
        helper(n-1, src, dest, aux, result)
        result.append([src, dest])
        helper(n-1, aux, src, dest, result)



print(tower_of_hanoi(4)) # Output: [[1, 2], [1, 3], [2, 3], [1, 2], [3, 1], [3, 2], [1, 2], [1, 3], [2, 3], [2, 1], [3, 1], [2, 3], [1, 2], [1, 3], [2, 3]]