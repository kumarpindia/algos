# This code defines a binary tree and an iterator to traverse the tree in-order (left, root, right).
# The BinaryTreeNode class represents a node in the binary tree, with a value and pointers to the left and
# right children.
# The TreeIterator class implements the in-order traversal using a stack to keep track of the nodes. The
# has_next() method checks if there are more nodes to visit
# and the next() method returns the value of the next node in the in-order traversal. 
# The implement_tree_iterator function takes the root of the binary tree and a list of operations (either "next"
# or "has_next") and returns a list of results corresponding to those operations.

# For example, if the operations are ["next", "has_next", "next"], the function will return a list of the
# next node's value, whether there are more nodes to visit, and the next node's value again.

# The code also includes a helper function to build a binary tree for testing purposes, and an example of how
# to use the implement_tree_iterator function with a sample binary tree and a list of operations.
# The code is designed to be efficient, with the next() method having an average time complexity of O(1) and
# the has_next() method having a time complexity of O(1). The space complexity of the TreeIterator is O(h),
# where h is the height of the binary tree, due to the stack used to keep track of the nodes.
# The code is also handling cases where the binary tree is empty or has only one node, and it correctly updates
# the stack when traversing the tree to ensure that the in-order traversal is maintained.

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TreeIterator:
    def __init__(self, root):
        self.stack_of_left_children = []
        self.push_left_children_to_stack(root)
    
    def push_left_children_to_stack(self, root):
        while root:
            self.stack_of_left_children.append(root)
            root = root.left
    
    def has_next(self):
        if bool(self.stack_of_left_children):
            return 1
        else:
            return 0

    def next(self):
        if not self.has_next():
            return 0
        result_node = self.stack_of_left_children.pop()
        self.push_left_children_to_stack(result_node.right)
        return result_node.value
        
def implement_tree_iterator(root, operations):
    ti = TreeIterator(root)
    result = []
    for op in operations:
        if op == "next":
            result.append(ti.next())
        else:
            result.append(ti.has_next())
        
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

root = BinaryTreeNode(100)
root.left = BinaryTreeNode(200)
root.right = BinaryTreeNode(300)
root.left.left = BinaryTreeNode(400)
root.left.right = BinaryTreeNode(500)
"""
root = BinaryTreeNode(200)
root.left = BinaryTreeNode(100)
root.right = BinaryTreeNode(300)

print(implement_tree_iterator(root, ["next", "has_next", "next", "next", "has_next", "has_next", "next"])) # Output: [100, 1, 200, 300, 0, 0, 0]