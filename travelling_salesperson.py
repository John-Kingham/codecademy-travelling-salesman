class Vertex:
    """
    A vertex for use in graphs.
    """

    def __init__(self, value):
        self.value = value
        self.edges = {}  # {vertex.value : weight}

    def add_edge(self, to_vertex_value, weight=0):
        """
        Adds an edge from this vertex to another.

        Parameters
        ----------
        to_vertex_value : str
            The Vertex.value of the neighbouring Vertex.
        weight : int
            The edge's weight.
        """
        self.edges[to_vertex_value] = weight

    def get_edges(self):
        """
        Returns Vertex.value for each neighbouring Vertex.

        Returns
        -------
        list : str
            Contains the Vertex.value of each neighbouring Vertex.
        """
        return list(self.edges.keys())

    def get_edge_weight(self, vertex_value):
        return self.edges[vertex_value]


class Graph:

    def __init__(self, directed=False):
        self.directed = directed
        self.vertices = {}  # {vertex.value : vertex object}

    def add_vertex(self, vertex):
        """
        Adds a vertex to the graph.

        Parameters
        ----------
        vertex : Vertex
        """
        self.vertices[vertex.value] = vertex

    def add_edge(self, from_vertex, to_vertex, weight=0):
        """
        Adds an edge between two vertices.
        If the graph isn't directed, an edge is added in both directions.

        Parameters
        ----------
        from_vertex : Vertex
        to_vertex : Vertex
        weight : int
        """
        self.vertices[from_vertex.value].add_edge(to_vertex.value, weight)
        if not self.directed:
            self.vertices[to_vertex.value].add_edge(from_vertex.value, weight)

    def has_path(self, from_vertex_value, to_vertex_value):
        """
        Returns whether the graph has a path between two vertices.

        Parameters
        ----------
        from_vertex_value : str
            Vertex.value for the from vertex
        to_vertex_value : str
            Vertex.value for the to vertex

        Returns
        -------
        bool
            True if a path exists between from and to, False if not.
        """
        vertices_to_visit = [from_vertex_value]
        seen = []
        while vertices_to_visit:
            vertex_value = vertices_to_visit.pop(0)
            seen.append(vertex_value)
            if vertex_value == to_vertex_value:
                return True
            neighbour_values = set(self.vertices[vertex_value].get_edges())
            for neighbour_value in neighbour_values:
                if neighbour_value not in seen:
                    vertices_to_visit.append(neighbour_value)
        return False
