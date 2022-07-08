import unittest
from singly_linked_list import SinglyLinkedList
from intersection import intersection


class TestIntersection(unittest.TestCase):
    def setUp(self):
        self.list1 = SinglyLinkedList()
        self.list1.add_to_tail(1)
        self.list1.add_to_tail(2)
        self.list1.add_to_tail(3)
        self.list1.add_to_tail(4)

        self.list2 = SinglyLinkedList()
        self.list2.add_to_tail(5)
        self.list2.add_to_tail(6)
        self.list2.add_to_tail(3)
        self.list2.add_to_tail(4)

    def test_intersection(self):
        self.assertEqual(intersection(self.list1, self.list2).data, 3)
