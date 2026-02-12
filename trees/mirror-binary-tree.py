# This function takes the root of a binary tree and modifies the tree in place to create its mirror image. The
# mirror image of a binary tree is a tree where the left and right children of all nodes are swapped. For
# example, if the original tree is:
#     1
#    / \
#   2   3
#  / \
# 4   5
# The mirror image of this tree would be:
#     1
#    / \
#   3   2
#      / \
#     5   4
# The function should return the root of the modified tree. Note: The function should modify the tree in place
# and return the root of the modified tree.
# The function should handle edge cases such as an empty tree (where the root is None) and a tree with only one
# node (where the left and right children are None). In these cases, the function should simply return the root
# without making any modifications.
# The function should also handle trees with multiple levels and varying numbers of children. For example, if the original tree is:
#     100 
#    /   \
#  200   300
#  / \   / \
# 400 500 250 350
# The mirror image of this tree would be:
#     100
#    /   \
#  300   200
#  / \   / \
# 350 250 500 400

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def mirror_image(root):
    
    q = [root]
    
    while q:
        cur_node = q.pop(0)
        cur_node.left, cur_node.right = cur_node.right, cur_node.left
        
        if cur_node.left:
            q.append(cur_node.left)
        if cur_node.right:
            q.append(cur_node.right)
            
    return root


# Helper to print the tree for testing
def print_tree_vars(node):
    if node is None:
        return
    print(vars(node))
    print_tree_vars(node.left)
    print_tree_vars(node.right)

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
root = BinaryTreeNode(200)
root.left = BinaryTreeNode(100)
root.right = BinaryTreeNode(300)
root.left.left = BinaryTreeNode(50)
root.left.right = BinaryTreeNode(150)
root.right.left = BinaryTreeNode(250)
root.right.right = BinaryTreeNode(350)

print("Original Tree:", print_tree_vars(root))
mirror_image(root)
print_tree_vars(root)