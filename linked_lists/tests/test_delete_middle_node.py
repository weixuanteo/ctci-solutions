import unittest
from singly_linked_list import SinglyLinkedList
from delete_middle_node import delete_middle_node

class TestDeleteMiddleNode(unittest.TestCase):
    def setUp(self):
        self.list1 = SinglyLinkedList()
        self.list1.add_to_tail(1)
        self.list1.add_to_tail(2)
        self.list1.add_to_tail(3)
        self.list1.add_to_tail(4)

        self.list2 = SinglyLinkedList()
        self.list2.add_to_tail(1)


    def test_delete_middle_node(self):
        delete_middle_node(self.list1.head.next)
        self.assertEqual(self.print_list(self.list1), "1-3-4")
        delete_middle_node(self.list2.head)
        self.assertEqual(self.print_list(self.list2), "1")

    def print_list(self, list):
        current = list.head
        result = ""
        while current:
            result += str(current.data) + "-"
            current = current.next
        return result[:-1]