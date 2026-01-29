# Given a list of maximum jump lengths from different houses, determine if you 
# can reach the last house in one or more jumps starting from the first one. 
# Maximum jump length of 2 from a house, for example, means that you can 
# either jump to the next house or to the one after next.

def can_reach_last_house(maximum_jump_lengths):
    # this one is time optimised. no more n-square time complexity
    no_of_house = len(maximum_jump_lengths)
    last_pos = no_of_house - 1
    for i in range(no_of_house - 2, -1, -1):
        if i + maximum_jump_lengths[i] >= last_pos:
            last_pos = i
    return last_pos == 0

print(can_reach_last_house([2, 3, 1, 0, 4, 7])) #should be 1/True
print(can_reach_last_house([2, 4, 1, 0, 2, 0, 1])) #should be 1/True
print(can_reach_last_house([3, 1, 1, 0, 2, 4])) #should be 0/False