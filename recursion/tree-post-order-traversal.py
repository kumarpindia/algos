# Given a binary tree, return the values of its nodes as an array in the order of a post-order traversal.
# Below is a recursive approach to solve the same problem.
# For example, for the following tree, you should return [4, 5, 2, 6, 7, 3, 1]:
#    1
#   / \
#  2   3
# / \   \
#4   5   6
#         \
#          7

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def postorder(root):
    result = []
    helper(root, result)
    return result
    
def helper(node, result):
    if node is None:
        return
    else:
        helper(node.left, result)
        helper(node.right, result)
        result.append(node.value)



# Helper to build the tree for testing

root = BinaryTreeNode(0)
root.left = BinaryTreeNode(1)
root.left.right = BinaryTreeNode(2)
root.left.right.left = BinaryTreeNode(4)
root.left.right.left.right = BinaryTreeNode(3)


print(postorder(root)) # Output: [3, 4, 2, 1, 0]