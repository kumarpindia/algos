# Given a set of people and a list of pairs of people who dislike each other, determine if it is
# possible to divide the people into two groups such that no pair of people in the same group dislike
# each other.

# Example 1:
# Input: num_of_people = 4, dislike1 = [0,1,2], dislike2 = [1,2,0]
# Output: false
# Explanation: It is not possible to divide the people into two groups such that no pair of people in the
# same group dislike each other.

def can_be_divided(num_of_people, dislike1, dislike2):
    if num_of_people <= 1:
        return True

    graph = [[] for _ in range(num_of_people)]
    color = [-1] * num_of_people
    
    for i in range(len(dislike1)):
        graph[dislike1[i]].append(dislike2[i])
        graph[dislike2[i]].append(dislike1[i])
    
    for i in range(num_of_people):
        if color[i] == -1:
            if not dfs(i, graph, color, 0):
                return False

    return True


def dfs(node, graph, color, node_color):
    if color[node] != -1:
        return True
    
    color[node] = node_color
    
    for neighbor in graph[node]:
        if color[neighbor] == color[node]:
            return False
        if not dfs(neighbor, graph, color, 1 - node_color):
            return False
        
    return True



print(can_be_divided(5, [0, 1, 1, 2, 3], [2, 2, 4, 3, 4])) # Output: True