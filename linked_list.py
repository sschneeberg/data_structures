nodeThree = {
    'next': None,
    'value': 3
}
nodeTwo = {
    'next': nodeThree,
    'value': 2
}
nodeOne = {
    'next': nodeTwo,
    'value': 1
}


def rev_linked_list(node, prev = None):
    if not node['next']: 
        node['next'] = prev
        return node
    else:
        next_node = node['next']
        node['next'] = prev
        return rev_linked_list(next_node, node)

rev_linked_list(nodeOne)

def iterative_rev(node):
    prev_node = None
    curr_node = node
    while curr_node != None:
        next_node = curr_node['next']
        curr_node['next'] = prev_node
        prev_node = curr_node
        curr_node = next_node
    return prev_node
        
iterative_rev(nodeThree)

assert(nodeOne == {'next': nodeTwo,'value': 1})