class Node:
    """ This is a binary tree node model for numeric values"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add_child(self, value, node):
        if self.value > value: # node goes to the left
            if not self.left: self.left = node # branch is empty, add it 
            else: self.left.add_child(value, node) # try again on the next node
        else: # node goes to the right
            if not self.right: self.right = node
            else: self.right.add_child(value, node)

class Binary_Tree: 
    """ Simple Binary Tree """
    def __init__(self):
        self.root = None

    def add_root(self, value):
        self.root = Node(value)

    def add_node(self, value):
        new_node = Node(value)
        self.root.add_child(value, new_node)

    def remove_node(self, value):
        self.root.remove_child(value)

    def depth_search(self, node, val):
        if node.value == val: return node
        if not node.left and not node.right: return node
        if node.value > val: # search left
            self.depth_search(node.left, val)
        else: # search right
            self.depth_search(node.right, val)

    def pre_order_print(self, root):
        values = []
        if root: 
            values.append(root.value)
            values = values + self.pre_order_print(root.left)
            values = values + self.pre_order_print(root.right)
        return values
        
    def in_order_print(self, root):
        values = []
        if root: 
            values = values + self.in_order_print(root.left) 
            values.append(root.value)
            values = values + self.in_order_print(root.right)
        return values

    def post_order_print(self, root):
        values = []
        if root: 
            values = values + self.post_order_print(root.left)
            values = values + self.post_order_print(root.right)
            values.append(root.value)
        return values

tree = Binary_Tree()

tree.add_root(27)
assert(tree.root.value == 27)
tree.add_node(14)
assert(tree.root.left.value == 14)
tree.add_node(35)
assert(tree.root.right.value == 35)
tree.add_node(10)
assert(tree.root.left.left.value == 10)
tree.add_node(19)
assert(tree.root.left.right.value == 19)
tree.add_node(31)
assert(tree.root.right.left.value == 31)
tree.add_node(42)
assert(tree.root.right.right.value == 42)


print('pre order')
print(tree.pre_order_print(tree.root))
assert(tree.pre_order_print(tree.root) == [27,14,10,19,35,31,42])
print('in order')
print(tree.in_order_print(tree.root))
assert(tree.in_order_print(tree.root) == [10,14,19,27,31,35,42])
print('post order')
print(tree.post_order_print(tree.root))
assert(tree.post_order_print(tree.root) == [10,19,14,31,42,35,27])
