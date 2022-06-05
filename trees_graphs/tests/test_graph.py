import unittest
from graph import Graph

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.graph.add_vertex(1)
        self.graph.add_vertex(2)
        self.graph.add_vertex(3)
        self.graph.add_vertex(4)
        self.graph.add_vertex(5)
    
    def setup_edges(self):
        one = self.graph.get_vertex_by_value(1)
        two = self.graph.get_vertex_by_value(2)
        three = self.graph.get_vertex_by_value(3)
        four = self.graph.get_vertex_by_value(4)
        five = self.graph.get_vertex_by_value(5)
        self.graph.add_edge(one, two)
        self.graph.add_edge(two, three)
        self.graph.add_edge(three, four)
        self.graph.add_edge(four, five)

    def test_add_vertex(self):
        self.assertEqual(self.graph.vertices[0].value, 1)
        self.assertEqual(self.graph.vertices[1].value, 2)
        self.assertEqual(self.graph.vertices[2].value, 3)
        self.assertEqual(self.graph.vertices[3].value, 4)
        self.assertEqual(self.graph.vertices[4].value, 5)
    
    def test_add_edge(self):
        self.setup_edges()
        self.assertEqual(self.graph.vertices[0].adj_list[0].value, 2)
        self.assertEqual(self.graph.vertices[1].adj_list[0].value, 3)
        self.assertEqual(self.graph.vertices[2].adj_list[0].value, 4)
        self.assertEqual(self.graph.vertices[3].adj_list[0].value, 5)
    
    def test_is_adjacent(self):
        self.setup_edges()
        one = self.graph.get_vertex_by_value(1)
        two = self.graph.get_vertex_by_value(2)
        three = self.graph.get_vertex_by_value(3)
        four = self.graph.get_vertex_by_value(4)
        five = self.graph.get_vertex_by_value(5)

        self.assertTrue(self.graph.is_adjacent(one, two))
        self.assertTrue(self.graph.is_adjacent(two, three))
        self.assertTrue(self.graph.is_adjacent(three, four))
        self.assertTrue(self.graph.is_adjacent(four, five))
        self.assertFalse(self.graph.is_adjacent(one, five))
        self.assertFalse(self.graph.is_adjacent(two, five))
        self.assertFalse(self.graph.is_adjacent(three, five))
    
    def test_delete_edge(self):
        self.setup_edges()
        one = self.graph.get_vertex_by_value(1)
        two = self.graph.get_vertex_by_value(2)
        three = self.graph.get_vertex_by_value(3)
        four = self.graph.get_vertex_by_value(4)
        five = self.graph.get_vertex_by_value(5)

        self.graph.delete_edge(one, two)
        self.assertFalse(self.graph.is_adjacent(one, two))
        self.graph.delete_edge(two, three)
        self.assertFalse(self.graph.is_adjacent(two, three))
        self.graph.delete_edge(three, four)
        self.assertFalse(self.graph.is_adjacent(three, four))
        self.graph.delete_edge(four, five)
        self.assertFalse(self.graph.is_adjacent(four, five))

    def test_delete_vertex(self):
        self.setup_edges()
        one = self.graph.get_vertex_by_value(1)        
        self.graph.delete_vertex(one)
        self.assertIsNone(self.graph.get_vertex_by_value(1))
    
    def test_is_empty(self):
        one = self.graph.get_vertex_by_value(1)
        two = self.graph.get_vertex_by_value(2)
        three = self.graph.get_vertex_by_value(3)
        four = self.graph.get_vertex_by_value(4)
        five = self.graph.get_vertex_by_value(5)

        self.assertFalse(self.graph.is_empty())
        self.graph.delete_vertex(one)
        self.graph.delete_vertex(two)
        self.graph.delete_vertex(three)
        self.graph.delete_vertex(four)
        self.graph.delete_vertex(five)
        self.assertTrue(self.graph.is_empty())