# This code defines a binary tree node class and a function to populate sibling pointers in a binary tree. The function uses a breadth-first traversal approach to connect each node to its next right sibling. The code also includes helper functions to print the tree and build a sample tree for testing.
# For example, given the following binary tree:
#         200
#        /   \
#      100   300
#     / \    / \
#    50 150 250 350
# After calling the populate_sibling_pointers function, the next_right pointers will be set as follows:
# - 200's next_right will be None
# - 100's next_right will point to 300
# - 300's next_right will be None
# - 50's next_right will point to 150
# - 150's next_right will point to 250
# - 250's next_right will point to 350
# - 350's next_right will be None 
# The function should return the root of the modified tree with sibling pointers populated.
# Note: The function should handle cases where the tree is empty (i.e., root is None) and should return None in such cases.

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def populate_sibling_pointers(root):
    if root is None:
        return None
    
    q = [root]
    prevnode = None
    
    while q:
        prevnode = None
        for _ in range(len(q)):
            cur_node = q.pop(0)
            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)
            if prevnode is not None:
                prevnode.next_right = cur_node
            prevnode = cur_node
        
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

populate_sibling_pointers(root)
print_tree_vars(root)