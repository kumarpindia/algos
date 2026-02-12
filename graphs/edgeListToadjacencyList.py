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

"""
        This approach is not working because the vertices are not in sorted order.
        For example, if edges = [[1, 2], [0, 1]], then when i = 0, left_vertex = 1 and right_vertex = 2.
        So, we will create adjacency list for vertex 1 and vertex 2. But when i = 1, left_vertex = 0 and right_vertex = 1.
        Now, we will create adjacency list for vertex 0. But vertex 1 is already done. So, we will skip it.
        Finally, the adjacency list will be [[], [0, 2], [1], []] which is incorrect.
        The correct adjacency list should be [[1], [0, 2], [1], []].
        Hence, we need to iterate through all edges for each vertex to create the adjacency list.
        
        left_vertex = edges[i][0]
        right_vertex = edges[i][1]
        adj_list_temp = []
            
        if left_vertex not in adj_list_made_of:
            for edge in edges:
                if left_vertex == edge[0]:
                    adj_list_temp.append(edge[1])
                if left_vertex == edge[1]:
                    adj_list_temp.append(edge[0])
            adj_list_temp.sort()
            adj_list_final.insert(left_vertex, adj_list_temp)
            adj_list_made_of.append(left_vertex)
        
        adj_list_temp = []

        if right_vertex not in adj_list_made_of:
            for edge in edges:
                if right_vertex == edge[0]:
                    adj_list_temp.append(edge[1])
                if right_vertex == edge[1]:
                    adj_list_temp.append(edge[0])
            adj_list_temp.sort()
            adj_list_final.insert(right_vertex, adj_list_temp)
            adj_list_made_of.append(right_vertex)
""" 


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
