# Given a binary tree and a number k, return whether there is a root-to-leaf path that sums up to k.
# For example, in the following tree, there are two root-to-leaf paths that sum to 7: 1 -> 2 -> 4 and
# 1 -> 3 -> 3.
#    1
#   / \
#  2   3
# / \   \
#4   5   3

#For reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def path_sum(root, k):
    queue_of_nodes = [root]
    sum_till_node = {root: root.value}
    
    while queue_of_nodes:
        curr_node = queue_of_nodes.pop(0)
        
        if curr_node.left is None and curr_node.right is None:
            if sum_till_node[curr_node] == k:
                return True
        if curr_node.left:
            sum_till_node[curr_node.left] = sum_till_node[curr_node] + curr_node.left.value
            queue_of_nodes.append(curr_node.left)
        if curr_node.right:
            sum_till_node[curr_node.right] = sum_till_node[curr_node] + curr_node.right.value
            queue_of_nodes.append(curr_node.right)
    
    return False


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

print(path_sum(root, 4))

#print_tree_vars(root)