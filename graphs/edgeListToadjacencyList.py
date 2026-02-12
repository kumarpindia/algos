# This is a function to convert edge list to adjacency list.

# The function takes in the number of vertices n and a list of edges, where each edge is represented as
# a list of two vertices [u, v]. The function returns an adjacency list representation of the graph,
# where each index in the list corresponds to a vertex and contains a list of its adjacent vertices.

# The function first initializes an empty adjacency list with n empty lists. It then iterates through
# each edge in the input list, adding the vertices to each other's adjacency lists. Finally, it sorts
# the adjacency lists for each vertex and returns the final adjacency list.

# Time complexity: O(n + m log m) where n is the number of vertices and m is the number of edges, due to
# the need to iterate through all edges and sort the adjacency lists for each vertex. The sorting step
# can be optimized to O(m) if we use a more efficient sorting algorithm or if we maintain the adjacency
# lists in sorted order as we build them.

def convert_edge_list_to_adjacency_list(n, edges):
    
    if n <= 1:
        return [[]]
    
    adj_list_final = [[] for _ in range(n)]
    
    for edge in edges:
        adj_list_final[edge[0]].append(edge[1])
        adj_list_final[edge[1]].append(edge[0])

        for i in range(n):
            adj_list_final[i].sort()
    
    return adj_list_final


#print(convert_edge_list_to_adjacency_list(5, [[0, 1], [1, 4], [1, 2], [1, 3], [3, 4]]))
#print(convert_edge_list_to_adjacency_list(2, [[0, 1]]))
print(convert_edge_list_to_adjacency_list(6, [
    [3, 5],
    [1, 0],
    [5, 2],
    [2, 4],
    [1, 2],
    [2, 3],
    [1, 5],
    [1, 3],
    [4, 3],
    [5, 4],
    [1, 4],
    [0, 5],
    [0, 3],
    [4, 0],
    [0, 2]
]))
