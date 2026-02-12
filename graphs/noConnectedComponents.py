# Given an undirected graph, find the number of connected components in the graph. The graph is given as
# an integer n, which is the number of vertices in the graph, and an array edges, where each 
# edges[i] = [a, b] indicates that there is an edge between a and b in the graph.

# Example 1:
# Input: n = 5, edges = [[0,1],[1,2],[0,2],[3,4]]
# Output: 2
# Explanation: There are two connected components in the graph, one component is {0,1,2} and the other
# component is {3,4}.

def number_of_connected_components(n, edges):
    
    graph = [[] for _ in range(n)]
    visited = [False] * n
    component_count = 0

    for vertex1, vertex2 in edges:
        graph[vertex1].append(vertex2)
        graph[vertex2].append(vertex1)
    
    dfs_helper(0, graph, visited)
    component_count = find_component_count(n, visited, graph)
    
    return component_count
    

def dfs_helper(vertex, graph, visited):
    visited[vertex] = True
    
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            dfs_helper(neighbor, graph, visited)


def find_component_count(n, visited, graph):
    component_count = 1
    for i in range(n):
        if not visited[i]:
            component_count += 1
            dfs_helper(i, graph, visited)

    return component_count
    

print(number_of_connected_components(5, [
[0, 1],
[1, 2],
[0, 2],
[3, 4]
])) # Output: 2