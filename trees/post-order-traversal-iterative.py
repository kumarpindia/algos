# Given a binary tree, return the values of its nodes as an array in the order of a post-order traversal.
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

def postorder_traversal(root):
    result = []
    helper_stack = [root]

    if root is None:
        return result
    
    while helper_stack:
        current_node = helper_stack.pop()
        result.append(current_node.value)
        if current_node.left:
            helper_stack.append(current_node.left)
        if current_node.right:
            helper_stack.append(current_node.right)
                
    result.reverse()
    return result


# Helper to build the tree for testing
"""
root = BinaryTreeNode(0)
root.left = BinaryTreeNode(1)
root.left.right = BinaryTreeNode(2)
root.left.right.left = BinaryTreeNode(4)
root.left.right.left.right = BinaryTreeNode(3)

root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)

root = BinaryTreeNode(100)
#root.left = BinaryTreeNode(None)
root.right = BinaryTreeNode(200)
"""
root = BinaryTreeNode(100)
root.left = BinaryTreeNode(200)
root.right = BinaryTreeNode(300)
root.left.left = BinaryTreeNode(400)
root.left.right = BinaryTreeNode(500)

print(postorder_traversal(root)) # Output: [400, 500, 200, 300, 100]