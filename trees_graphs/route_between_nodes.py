# Given a directed graph, design an algorithm to find out whether there is a route
# between two nodes.

from queue import MyQueue
from graph import Vertex


def is_route_between_nodes(start: Vertex, end: Vertex) -> bool:
    visited = set()
    queue = MyQueue()
    queue.enqueue(start)
    while not queue.is_empty():
        node = queue.dequeue()
        vertex = node.data
        if vertex == end:
            return True
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in vertex.adj_list:
                queue.enqueue(neighbor)
    return False
