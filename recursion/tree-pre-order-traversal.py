# Given a binary tree, return the values of its nodes as an array in the order of a pre-order traversal.
# Below is a recursive approach to solve the same problem.
# For example, for the following tree, you should return [1, 2, 4, 3]:
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

def preorder(root):
    result = []
    helper(root, result)
    return result

def helper(node, result):
    if node is None:
        return
    else:
        result.append(node.value)
        helper(node.left, result)
        helper(node.right, result)


# Helper to build the tree for testing

root = BinaryTreeNode(0)
root.left = BinaryTreeNode(1)
root.left.right = BinaryTreeNode(2)
root.left.right.left = BinaryTreeNode(4)
root.left.right.left.right = BinaryTreeNode(3)

print(preorder(root)) # Output: [0, 1, 2, 4, 3]