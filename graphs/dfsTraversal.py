# DFS Traversal of a Graph is a method of traversing or searching through a graph data structure. It
# starts at a given vertex and explores as far as possible along each branch before backtracking. This
# process continues until all vertices have been visited. The DFS traversal can be implemented using a
# stack data structure to keep track of the vertices to be explored next, or it can be implemented
# recursively. The algorithm marks each vertex as visited to avoid processing the same vertex
# multiple times.

# The DFS traversal is useful for solving problems such as finding connected components, topological
# sorting, and detecting cycles in a graph. It can also be used to perform depth-first search on a tree
# data structure.

# Given an undirected graph, represented as an edge list, perform a depth-first search (DFS) traversal
# of the graph. The graph has n vertices, numbered from 0 to n-1. The edge list is given as a list of
# pairs of vertices, where each pair [u, v] represents an undirected edge between vertices u and v.
# The DFS traversal should start from the vertex with the smallest number (i.e., vertex 0) and visit all
# reachable vertices in the graph. If there are multiple vertices to visit at the same level, they
# should be visited in ascending order of their vertex numbers. The function should return a list of
# vertices in the order they were visited during the DFS traversal.

# Time complexity: O(V + E) where V is the number of vertices and E is the number of edges in the graph,
# due to the need to visit each vertex and edge once. The space complexity is O(V) for the visited array
# and the call stack used for recursion.

def dfs_traversal(n, edges):    
    visited = [False] * n
    graph = [[] for _ in range(n)]
    result = []
    
    for vertex1, vertex2 in edges:
        graph[vertex1].append(vertex2)
        graph[vertex2].append(vertex1)

    for i in range(n):
        if not visited[i]:
            dfs_traversal_helper(i, graph, visited, result)
    
    return result


def dfs_traversal_helper(vertex, graph, visited, result):
    visited[vertex] = True
    result.append(vertex)

    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            dfs_traversal_helper(neighbor, graph, visited, result)



print(dfs_traversal(6, [
[0, 1],
[0, 2],
[1, 4],
[3, 5]
]))