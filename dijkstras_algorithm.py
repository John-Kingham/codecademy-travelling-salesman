from heapq import heappush, heappop
import math


def dijkstras(graph, start):
    """
    Dijkstra's algorithm, which returns the lowest-weight path to each Vertex.

    Parameters
    ----------
    graph : dict
        Key (str) = Vertex name.
        Value (list) = List of edges as tuples (vertex_name, weight).
    start : string
        Name of the start vertex.

    Returns
    -------
    dict
        Key (str) = Vertex name.
        Value (float) = Lowest path weight from start.
    """
    path_weights = {}
    for vertex in graph:
        path_weights[vertex] = math.inf
    path_weights[start] = 0
    vertices_to_explore = [(path_weights[start], start)]
    while vertices_to_explore:
        weight, vertex = heappop(vertices_to_explore)
        for neighbour, edge_weight in graph[vertex]:
            new_weight = weight + edge_weight
            if new_weight < path_weights[neighbour]:
                path_weights[neighbour] = new_weight
                heappush(vertices_to_explore, (new_weight, neighbour))
    return path_weights
