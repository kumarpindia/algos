# BFS Traversal of a Graph is a method of traversing or searching through a graph data structure. It
# starts at a given vertex and explores all its neighbors before moving on to the neighbors' neighbors.
# This process continues until all vertices have been visited. The BFS traversal can be implemented using a queue data structure to keep track of the vertices to be
# explored next. The algorithm marks each vertex as visited to avoid processing the same vertex
# multiple times.

# The BFS traversal is useful for finding the shortest path between two vertices in an unweighted graph,
# as it explores all vertices at the present depth level before moving on to the next level. It can also
# be used to check if a graph is bipartite, to find connected components, and to perform level-order
# traversal of a tree.

# Given an undirected graph, represented as an edge list, perform a breadth-first search (BFS) traversal
# of the graph. The graph has n vertices, numbered from 0 to n-1. The edge list is given as a list of pairs of vertices, where each pair [u, v] represents an undirected
# edge between vertices u and v. The BFS traversal should start from the vertex with the smallest number
# (i.e., vertex 0) and visit all reachable vertices in the graph. If there are multiple vertices to
# visit at the same level, they should be visited in ascending order of their vertex numbers.
# The function should return a list of vertices in the order they were visited during the BFS traversal

# Time complexity: O(V + E) where V is the number of vertices and E is the number of edges in the graph,
# due to the need to visit each vertex and edge once. The space complexity is O(V) for the visited array
# and the queue used for traversal.

def bfs_traversal(n, edges):
    graph = [[] for _ in range(n)]
    visited = [False] * n
    result = []
    
    for vertex1, vertex2 in edges:
        graph[vertex1].append(vertex2)
        graph[vertex2].append(vertex1)

    for i in range(n):
        if not visited[i]:
            bfs_traversal_helper(i, graph, visited, result)

    return result

def bfs_traversal_helper(start_vertex, graph, visited, result):
    visited[start_vertex] = True
    result.append(start_vertex)
    queue = [start_vertex]

    while queue:
        current_vertex = queue.pop(0)
        for neighbor in graph[current_vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                result.append(neighbor)
                queue.append(neighbor)





print(bfs_traversal(6, [
[0, 1],
[0, 2],
[0, 4],
[2, 3]
]))