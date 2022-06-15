import unittest
from build_order import create_build_order

class TestBuildOrder(unittest.TestCase):
    def setUp(self):
        self.projects1 = ['a', 'b', 'c', 'd', 'e', 'f']
        self.dependencies1 = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
        self.projects2 = ['a', 'b', 'c', 'd', 'e', 'f']
        self.dependencies2 = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c'), ('c', 'a')]
    
    def test_build_order(self):
        build_order = create_build_order(self.projects1, self.dependencies1)
        self.assertEqual(build_order, ['f', 'a', 'b', 'd', 'c', 'e'])
    
    def test_build_order_no_valid_order(self):
        build_order = create_build_order(self.projects2, self.dependencies2)
        self.assertEqual(build_order, None)