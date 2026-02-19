# Given a binary tree, return an array of all its root-to-leaf paths. Each path should be represented as an array of node values.
# Below is a recursive approach to solve the same problem.
# For example, for the following tree, you should return [[1, 2, 4], [1, 3]]:
#    1
#   / \
#  2   3
# /
#4

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def all_paths_of_a_binary_tree(root):
    
    result = []
    path = []
    helper(root, path, result)
    return result
    
def helper(root, path, result):
    if root is None:
        return
    path.append(root.value)
    if root.left is None and root.right is None:
        result.append(path[:])
        return
    else:
        if root.left:
            helper(root.left, path, result)
            path.pop()  # Backtrack to remove last value
        if root.right:
            helper(root.right, path, result)
            path.pop()  # Backtrack to remove last value


# Helper to build the tree for testing
"""
root = BinaryTreeNode(0)
root.left = BinaryTreeNode(1)
root.left.right = BinaryTreeNode(2)
root.left.right.left = BinaryTreeNode(4)
root.left.right.left.right = BinaryTreeNode(3)
"""

root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)


print(all_paths_of_a_binary_tree(root)) # Output: [[1, 2, 4], [1, 2, 5], [1, 3, 6], [1, 3, 7]]