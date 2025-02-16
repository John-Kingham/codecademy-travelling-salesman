class Vertex:

    def __init__(self, value):
        self.value = value
        self.edges = {}  # {vertex.value : weight}

    def add_edge(self, vertex_value, weight):
        self.edges[vertex_value] = weight

    def get_edges(self):
        return list(self.edges.keys())

    def get_edge_weight(self, vertex_value):
        return self.edges[vertex_value]


class Graph:

    def __init__(self, directed=False):
        self.directed = directed
        self.adjacency_list = {}  # {vertex.value : vertex object}

    def add_vertex(self, vertex):
        pass
        # TODO finish this off