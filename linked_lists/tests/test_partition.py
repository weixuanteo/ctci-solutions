import unittest

from singly_linked_list import SinglyLinkedList
from partition import partition


class TestPartition(unittest.TestCase):
    def setUp(self):
        self.list1 = SinglyLinkedList()
        self.list1.add_to_tail(3)
        self.list1.add_to_tail(5)
        self.list1.add_to_tail(8)
        self.list1.add_to_tail(5)
        self.list1.add_to_tail(10)
        self.list1.add_to_tail(2)
        self.list1.add_to_tail(1)

        self.list2 = SinglyLinkedList()
        self.list2.add_to_tail(3)
        self.list2.add_to_tail(5)
        self.list2.add_to_tail(3)
        self.list2.add_to_tail(5)
        self.list2.add_to_tail(3)
        self.list2.add_to_tail(5)

    def test_partition(self):
        self.assertEqual(self.print_list(partition(self.list1, 5)), "3-2-1-5-8-5-10")
        self.assertEqual(self.print_list(partition(self.list2, 4)), "3-3-3-5-5-5")

    def print_list(self, list):
        result = ""
        current = list.head
        while current:
            result += str(current.data) + "-"
            current = current.next
        return result[:-1]
