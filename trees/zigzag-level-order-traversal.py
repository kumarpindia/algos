# This is an implementation of zigzag level order traversal for a binary tree.
# The function zigzag_level_order_traversal takes the root of a binary tree as input and returns a list of
# lists, where each inner list contains the values of the nodes at that level
# in zigzag order (i.e., left to right for the first level, right to left for the second level, and so on).
# For example, given the following binary tree:
#         0
#       /   \
#      1     2
#     / \   / 
#    3   4 2
# The zigzag level order traversal of this tree would be [[0], [2, 1], [3, 4]], since the first level is
# traversed from left to right, the second level is traversed from right to left, and the third level is
# traversed from left to right.
# Note: The function should handle cases where the tree is empty (i.e., root is None) and should return an
# empty list in such cases.
# The BinaryTreeNode class is defined to represent a node in the binary tree, with attributes for the node's
# value and pointers to its left and right children.
# The function uses a queue to perform a level order traversal of the tree, and a variable run_count to keep
# track of the current level and determine whether to reverse the order of the values at that level.
# The helper functions print_tree_vars and the commented-out code for building sample trees are included for
# testing purposes, allowing you to visualize the structure of the tree and verify the correctness of the
# zigzag level order traversal.
# The zigzag_level_order_traversal function should return the correct zigzag level order traversal for any
# given binary tree, including edge cases such as an empty tree or a tree with only one node.

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def zigzag_level_order_traversal(root):
    if root is None:
        return []
    
    result = []
    q_of_nodes = [root]
    run_count = 1

    while q_of_nodes:
        q_of_nodes_size = len(q_of_nodes)
        curr_level_values = []
            
        for i in range(q_of_nodes_size):
            curr_node = q_of_nodes.pop(0)
            curr_level_values.append(curr_node.value)
            if curr_node.left:
                q_of_nodes.append(curr_node.left)
            if curr_node.right:
                q_of_nodes.append(curr_node.right)
                
        if run_count % 2 == 0:
            curr_level_values.reverse()
        result.append(curr_level_values)
        run_count += 1
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

root = BinaryTreeNode(1)
root.right = BinaryTreeNode(3)
root.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)

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
root = BinaryTreeNode(0)
root.left = BinaryTreeNode(1)
root.right = BinaryTreeNode(2)
root.left.left = BinaryTreeNode(3)
root.left.right = BinaryTreeNode(4)
root.right = BinaryTreeNode(2)

print(zigzag_level_order_traversal(root)) # Output: [[0], [2, 1], [3, 4]]

#print_tree_vars(root)