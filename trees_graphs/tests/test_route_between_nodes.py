import unittest
from route_between_nodes import is_route_between_nodes
from graph import *

class TestIsRouteBetweenNodes(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        a = Vertex('A')
        b = Vertex('B')
        c = Vertex('C')
        d = Vertex('D')
        e = Vertex('E')
        f = Vertex('F')
        g = Vertex('G')
        self.graph.add_vertex(a)
        self.graph.add_vertex(b)
        self.graph.add_vertex(c)
        self.graph.add_vertex(d)
        self.graph.add_vertex(e)
        self.graph.add_vertex(f)
        self.graph.add_vertex(g)
        self.graph.add_edge(a, b)
        self.graph.add_edge(a, c)
        self.graph.add_edge(a, g)
        self.graph.add_edge(b, d)
        self.graph.add_edge(c, e)
        self.graph.add_edge(d, e)
        self.graph.add_edge(d, f)

        # a -> b -> d -> e
        # a -> c -> e
        # a -> b -> d -> f
        # a -> g

    def test_is_route_between_nodes(self):
        a = self.graph.get_vertex_by_value('A')
        d = self.graph.get_vertex_by_value('D')
        e = self.graph.get_vertex_by_value('E')
        g = self.graph.get_vertex_by_value('G')

        self.assertTrue(is_route_between_nodes(a, d))
        self.assertTrue(is_route_between_nodes(a, e))
        self.assertTrue(is_route_between_nodes(a, g))
        self.assertTrue(is_route_between_nodes(d, e))
        self.assertFalse(is_route_between_nodes(d, g))
        self.assertFalse(is_route_between_nodes(e, g))
        


