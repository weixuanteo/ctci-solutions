import unittest
from singly_linked_list import SinglyLinkedList

class TestSinglyLinkedList(unittest.TestCase):
    def test_add_to_head(self):
        ll = SinglyLinkedList()
        ll.add_to_head(1)
        ll.add_to_head(2)
        ll.add_to_head(3)
        self.assertEqual(ll.head.data, 3)
        self.assertEqual(ll.head.next.data, 2)
        self.assertEqual(ll.head.next.next.data, 1)
        self.assertEqual(ll.size, 3)

    def test_add_to_tail(self):
        ll = SinglyLinkedList()
        ll.add_to_tail(1)
        ll.add_to_tail(2)
        ll.add_to_tail(3)
        self.assertEqual(ll.head.data, 1)
        self.assertEqual(ll.head.next.data, 2)
        self.assertEqual(ll.head.next.next.data, 3)
        self.assertEqual(ll.size, 3)

    def test_remove_from_head(self):
        ll = SinglyLinkedList()
        ll.add_to_head(1)
        removed_node = ll.remove_from_head()
        self.assertEqual(removed_node.data, 1)
        self.assertEqual(ll.head, None)
        self.assertEqual(ll.tail, None)
        self.assertEqual(ll.size, 0)

        ll = SinglyLinkedList()
        ll.add_to_tail(1)
        ll.add_to_tail(2)
        ll.remove_from_head()
        self.assertEqual(ll.head.data, 2)
        self.assertEqual(ll.tail.data, 2)
        self.assertEqual(ll.size, 1)