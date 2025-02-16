import unittest
from dijkstras_algorithm import dijkstras


class TestDijkstrasAlgorithm(unittest.TestCase):

    def setUp(self):
        self.test_graph = {
            "A": [("B", 5), ("C", 3)],
            "B": [("C", 3), ("D", 2)],
            "C": [("D", 2), ("E", 5)],
            "D": [("E", 1)],
            "E": [("A", 7)],
        }

    def test_djikstras_from_first_vertex(self):
        shortest_from_a = {"A": 0, "B": 5, "C": 3, "D": 5, "E": 6}
        self.assertEqual(dijkstras(self.test_graph, "A"), shortest_from_a)

    def test_djikstras_from_last_vertex(self):
        shortest_from_e = {'A': 7, 'B': 12, 'C': 10, 'D': 12, 'E': 0}
        self.assertEqual(dijkstras(self.test_graph, "E"), shortest_from_e)
