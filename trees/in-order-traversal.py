# Given a binary tree, return the values of its nodes as an array in the order of an in-order traversal.
# For example, for the following tree, you should return [3, 2, 4, 1, 5]:
#    1
#   / \
#  2   5
# / \
#3   4

# For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inorder(root):
    
    result = []
    helper(root, result)
    return result
    
def helper(node, result):
    if node is None:
        return
    else:
        helper(node.left, result)
        result.append(node.value)
        helper(node.right, result)


# Helper to build the tree for testing

root = BinaryTreeNode(0)
root.left = BinaryTreeNode(1)
root.left.right = BinaryTreeNode(2)
root.left.right.left = BinaryTreeNode(4)
root.left.right.left.right = BinaryTreeNode(3)


print(inorder(root)) # Output: [1, 4, 3, 2, 0]