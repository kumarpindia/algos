# Given the root of a binary search tree and a value, determine if the value exists in the tree. Return true if
# it does, otherwise return false.
# A binary search tree is a binary tree in which for each node, any descendant of node.left has a value
# strictly less than node.value, and any descendant of node.right has a value strictly greater than node.value.
# It follows that there are no duplicate values in the tree.
# For example, for the following tree:
#     2
#    / \
#   1   5
#      / \
#     4   6
# The value 4 exists in the tree, but the value 3 does not exist in the tree. Therefore, for the value 4, you
# should return true, while for the value 3, you should return false.


# For your reference:
# Definition for a binary tree node.
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def search_node_in_bst(root, value):
    if root is None:
        return False
    
    if root.value == value:
        return True
    else:
        new_root = root.left if value < root.value else root.right
        return search_node_in_bst(new_root, value)


# Helper to build the tree for testing
root = BinaryTreeNode(2)
root.left = BinaryTreeNode(1)
root.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(4)
root.right.right = BinaryTreeNode(6)

print(search_node_in_bst(root, 4)) # Output: True
print(search_node_in_bst(root, 3)) # Output: False