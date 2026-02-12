# Given a binary tree and two values a and b, find the lowest common ancestor (LCA) of the two nodes in
# the tree. The LCA is defined as the lowest node in the tree that has both a and b as descendants
# (where we allow a node to be a descendant of itself).
# For example, in the following binary tree, the LCA of 4 and 5 is 2, and the LCA of 4 and 6 is 1.
#         1
#        / \
#       2   3
#      / \
#     4   5
#    /
#   6
# You can assume that both a and b are present in the tree, and all values in the tree are unique.

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def lca(root, a, b):
    
    # normalize to values if nodes were passed
    def _get_val(x):
        return getattr(x, "value", x)
    a_val = _get_val(a)
    b_val = _get_val(b)

    def helper(root):
        if root is None:
            return None, False, False
        left_ancestor, a_found_left, b_found_left = helper(root.left)
        right_ancestor, a_found_right, b_found_right = helper(root.right)
        a_found = a_found_left or a_found_right or root.value == a_val
        b_found = b_found_left or b_found_right or root.value == b_val
        if root.value == a_val or root.value == b_val:
            return root.value, a_found, b_found
        if left_ancestor and right_ancestor:
            return root.value, a_found, b_found
        if left_ancestor:
            return left_ancestor, a_found, b_found
        if right_ancestor:
            return right_ancestor, a_found, b_found
        return None, a_found, b_found
        
    ancestor, _, _ = helper(root)
    return ancestor


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

root = BinaryTreeNode(100)
root.left = BinaryTreeNode(200)
root.right = BinaryTreeNode(300)
root.left.left = BinaryTreeNode(400)
root.left.right = BinaryTreeNode(500)
"""
root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)

print(lca(root, 1, 2)) # Output: 1