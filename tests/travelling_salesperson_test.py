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

    @unittest.skip("skip due to partial implementation")
    def test_has_path(self):
        graph = Graph()
        graph.add_vertex(self.vertex)
        self.fail()
