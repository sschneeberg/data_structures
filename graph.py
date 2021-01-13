class Graph:
    """ This is a simple graph using adjacency lists """

    def __init__(self, values):
        self.values = {}
        for i in values: 
            self.values[i] = []

    def add_edge_directed(self, node, to):
        if not self.values[node]: raise ValueError("Node does not exist")
        self.values[node].append(to)

    def add_edge_undirected(self, node, to):
        if not self.values[node]: raise ValueError("Node does not exist")
        if not self.values[to]: raise ValueError("Node to connect does not exist")
        self.values[node].append(to)
        self.values[to].append(node)

    def add_node(self, value):
        if value in self.values: raise ValueError("Node already in graph")
        self.values[value] = []
