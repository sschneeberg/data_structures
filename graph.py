class Graph:
    """ This is a simple graph using adjacency lists """

    def __init__(self, values):
        self.values = {}
        for i in values: 
            self.values[i] = []

    def add_edge_directed(self, src, dest):
        if not self.values[src]: raise ValueError("Node does not exist")
        self.values[src].append(dest)

    def add_edge_undirected(self, src, dest):
        if not self.values[src]: raise ValueError("Node does not exist")
        if not self.values[dest]: raise ValueError("Node to connect does not exist")
        self.values[src].append(dest)
        self.values[dest].append(src)

    def add_node(self, value):
        if value in self.values: raise ValueError("Node already in graph")
        self.values[value] = []