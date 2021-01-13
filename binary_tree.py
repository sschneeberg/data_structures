class Node:
    """ This is a binary tree node model """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def depth_search(node, val):
    if node.value == val: return node
    if not node.left and not node.right: return node
    if node.value > val: # search left
        depth_search(node.left, val)
    else: # search right
        depth_search(node.right, val)