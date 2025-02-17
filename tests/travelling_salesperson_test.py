import unittest
from travelling_salesperson import Vertex, Graph


class TestVertex(unittest.TestCase):

    def setUp(self):
        self.vertex = Vertex("A")
        self.vertex.add_edge("B", 3)
        self.vertex.add_edge("C", 5)

    def test_get_edges(self):
        self.assertEqual(self.vertex.get_edges(), ["B", "C"])

    def test_get_edge_weight(self):
        self.assertEqual(self.vertex.get_edge_weight("C"), 5)


class TestGraph(unittest.TestCase):

    def test_has_path_to_direct_neighbour(self):
        graph = Graph()
        vertex_a = Vertex("A")
        vertex_b = Vertex("B")
        vertex_c = Vertex("C")
        graph.add_vertex(vertex_a)
        graph.add_vertex(vertex_b)
        graph.add_vertex(vertex_c)
        graph.add_edge(vertex_a, vertex_b)
        graph.add_edge(vertex_b, vertex_c)
        self.assertTrue(graph.has_path(vertex_a.value, vertex_b.value))

    def test_has_path_to_indirect_vertex(self):
        graph = Graph()
        vertex_a = Vertex("A")
        vertex_b = Vertex("B")
        vertex_c = Vertex("C")
        graph.add_vertex(vertex_a)
        graph.add_vertex(vertex_b)
        graph.add_vertex(vertex_c)
        graph.add_edge(vertex_a, vertex_b)
        graph.add_edge(vertex_b, vertex_c)
        self.assertTrue(graph.has_path(vertex_a.value, vertex_c.value))

    def test_no_path(self):
        graph = Graph()
        vertex_a = Vertex("A")
        vertex_b = Vertex("B")
        graph.add_vertex(vertex_a)
        graph.add_vertex(vertex_b)
        self.assertFalse(graph.has_path(vertex_a.value, vertex_b.value))

    def test_undirected_graph_makes_bidirectional_edges(self):
        graph = Graph()
        vertex_a = Vertex("A")
        vertex_b = Vertex("B")
        graph.add_vertex(vertex_a)
        graph.add_vertex(vertex_b)
        graph.add_edge(vertex_a, vertex_b)
        self.assertTrue(graph.has_path(vertex_b.value, vertex_a.value))

    def test_directed_graph_makes_unidirectional_edges(self):
        graph = Graph(True)
        vertex_a = Vertex("A")
        vertex_b = Vertex("B")
        graph.add_vertex(vertex_a)
        graph.add_vertex(vertex_b)
        graph.add_edge(vertex_a, vertex_b)
        self.assertFalse(graph.has_path(vertex_b.value, vertex_a.value))
