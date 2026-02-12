# This code defines a binary tree and a function to compute the right side view of the tree. The right side
# view consists of the nodes that are visible when the tree is viewed from the right side.
# The function uses a breadth-first traversal approach to visit each level of the tree and collects the last
# node of each level, which represents the rightmost node at that level. The code also includes helper
# functions to print the tree and build a sample tree for testing.

# For example, given the following binary tree:
#         1
#       /   \
#      4     3
#       \   / \
#        5 6   7
# The right side view of this tree would be [1, 3, 7], since those are the nodes visible from the right side.
# The function should return a list of values representing the right side view of the tree.

# Note: The function should handle cases where the tree is empty (i.e., root is None) and should return an
# empty list in such cases.

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def right_view(root):

    result = []
    q = [root]

    while q:
        curr_level_q_size = len(q)
    
        for i in range(curr_level_q_size):
            curr_node = q.pop(0)        
            if (i == curr_level_q_size-1):
                result.append(curr_node.value)
            if curr_node.left:
                q.append(curr_node.left)
            if curr_node.right:
                q.append(curr_node.right)
        
    return result


# Helper to print the tree for testing
def print_tree_vars(node):
    if node is None:
        return
    print(vars(node))
    print_tree_vars(node.left)
    print_tree_vars(node.right)

# Helper to build the tree for testing
"""
root = BinaryTreeNode(1)
root.children.append(BinaryTreeNode(3))
root.children.append(BinaryTreeNode(4))
root.children.append(BinaryTreeNode(2))
root.children[1].children.append(BinaryTreeNode(5))
root.children[1].children.append(BinaryTreeNode(6))
"""
root = BinaryTreeNode(1)
root.right = BinaryTreeNode(3)
root.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)
"""
root = BinaryTreeNode(2)
root.left = BinaryTreeNode(5)
root.right = BinaryTreeNode(4)
root.left.left = BinaryTreeNode(0)
root.left.right = BinaryTreeNode(1)
root.right.left = BinaryTreeNode(3)
root.right.right = BinaryTreeNode(6)

root = BinaryTreeNode(0)
root.left = BinaryTreeNode(1)
root.left.right = BinaryTreeNode(2)
root.left.right.left = BinaryTreeNode(4)
root.left.right.left.right = BinaryTreeNode(3)

root = BinaryTreeNode(100)
#root.left = BinaryTreeNode(None)
root.right = BinaryTreeNode(200)

root = BinaryTreeNode(100)
root.left = BinaryTreeNode(200)
root.right = BinaryTreeNode(300)
root.left.left = BinaryTreeNode(400)
root.left.right = BinaryTreeNode(500)

root = BinaryTreeNode(200)
root.left = BinaryTreeNode(100)
root.right = BinaryTreeNode(300)
root.left.left = BinaryTreeNode(50)
root.left.right = BinaryTreeNode(150)
root.right.left = BinaryTreeNode(250)
root.right.right = BinaryTreeNode(350)
"""

print(right_view(root)) # Output: [1, 3, 7]
#print_tree_vars(root)