# Given a graph with n nodes and a list of edges, determine if the graph is a tree.
# A tree is a connected graph with no cycles. This means that for a graph to be a tree, it must have 
# exactly n-1 edges and be fully connected.

# The function first constructs the graph using an adjacency list representation. It then performs a 
# depth-first search (DFS) to detect any cycles in the graph. If a cycle is detected, the function 
# returns False. Finally, it checks if the graph is fully connected and has the correct number of edges 
# to determine if it is a tree.

# Example usage is provided at the end, where the function is called with different sets of nodes and 
# edges to check if the resulting graph is a tree.

# Time complexity: O(n) where n is the number of nodes in the graph, due to the DFS traversal and the 
# checks for connectivity and edge count. 

def is_it_a_tree(node_count, edge_start, edge_end):
    
    graph = [[] for _ in range(node_count)]
    visited = [False] * node_count
    
    for i in range(len(edge_start)):
        graph[edge_start[i]].append(edge_end[i])
        graph[edge_end[i]].append(edge_start[i])

    for i in range(node_count):
        if not visited[i]:
            if dfs_detect_cycle(i, -1, graph, visited):
                return False
    
    return check_is_connected(node_count, visited) and len(edge_start) == node_count - 1

            
def dfs_detect_cycle(vertex, parent, graph, visited):
    visited[vertex] = True
    
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            if dfs_detect_cycle(neighbor, vertex, graph, visited):
                return True
        elif neighbor != parent:
            return True
    
    return False


def check_is_connected(node_count, visited):
    for i in range(node_count):
        if not visited[i]:
            return False
    
    return True
    

print(is_it_a_tree(4, [0, 0, 0], [1, 2, 3]))
print(is_it_a_tree(4, [0, 0], [1, 2]))