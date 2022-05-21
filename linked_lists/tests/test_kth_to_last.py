import unittest
from singly_linked_list import SinglyLinkedList
from kth_to_last import return_kth_to_last, return_kth_to_last_ptr

class TestKthToLast(unittest.TestCase):
    def setUp(self) -> None:
        self.list1 = SinglyLinkedList()
        self.list1.add_to_tail(1)
        self.list1.add_to_tail(2)
        self.list1.add_to_tail(3)
        self.list1.add_to_tail(4)
        self.list1.add_to_tail(5)
    
    def test_return_kth_to_last(self):
        self.assertEqual(return_kth_to_last(self.list1, 1), 5)
        self.assertEqual(return_kth_to_last(self.list1, 2), 4)
        self.assertEqual(return_kth_to_last(self.list1, 3), 3)
        self.assertEqual(return_kth_to_last(self.list1, 4), 2)
        self.assertEqual(return_kth_to_last(self.list1, 5), 1)
        self.assertEqual(return_kth_to_last(self.list1, 6), None)
    
    def test_return_kth_to_last_ptr(self):
        self.assertEqual(return_kth_to_last_ptr(self.list1, 1), 5)
        self.assertEqual(return_kth_to_last_ptr(self.list1, 2), 4)
        self.assertEqual(return_kth_to_last_ptr(self.list1, 3), 3)
        self.assertEqual(return_kth_to_last_ptr(self.list1, 4), 2)
        self.assertEqual(return_kth_to_last_ptr(self.list1, 5), 1)
        self.assertEqual(return_kth_to_last_ptr(self.list1, 6), None)