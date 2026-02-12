# Given an undirected graph, represented as an edge list, convert it to an adjacency matrix. The graph
# has n vertices, numbered from 0 to n-1.

# The edge list is given as a list of pairs of vertices, where each pair [u, v] represents an undirected
# edge between vertices u and v. The adjacency matrix should be a 2D list of booleans, where the value at
# index [i][j] is True if there is an edge between vertices i and j, and False otherwise. The diagonal
# entries of the adjacency matrix should be False, since there are no self-loops in the graph. 

# The function should return the adjacency matrix as a 2D list of booleans. 

# Time complexity: O(n^2 + m) where n is the number of vertices and m is the number of edges, due to the
# need to initialize the adjacency matrix and iterate through all edges to populate it. The space
# complexity is O(n^2) for the adjacency matrix.

def convert_edge_list_to_adjacency_matrix(n, edges):
    
    if n <= 0:
        return [[]]
    
    adj_matrix = [[bool(0) for _ in range(n)] for _ in range(n)]
    
    for edge in edges:
        adj_matrix[edge[0]][edge[1]] = bool(1)
        adj_matrix[edge[1]][edge[0]] = bool(1)
    
    return adj_matrix


#print(convert_edge_list_to_adjacency_matrix(3, [[0, 1], [1, 2], [2, 0]]))
print(convert_edge_list_to_adjacency_matrix(5, [
[0, 1],
[1, 4],
[1, 2],
[1, 3],
[3, 4]
]))