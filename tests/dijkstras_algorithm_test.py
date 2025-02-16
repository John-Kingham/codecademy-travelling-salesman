import unittest
from dijkstras_algorithm import dijkstras


class TestDijkstrasAlgorithm(unittest.TestCase):

    def test_djikstras_algorithm(self):
        test_graph = {
            "A": [("B", 5), ("C", 3)],
            "B": [("C", 3), ("D", 2)],
            "C": [("D", 2), ("E", 5)],
            "D": [("E", 1)],
            "E": [("A", 7)],
        }
        shortest_distances = {"A": 0, "B": 5, "C": 3, "D": 5, "E": 6}
        self.assertEqual(dijkstras(test_graph, "A"), shortest_distances)
