import unittest
from singly_linked_list import SinglyLinkedList
from sum_lists import sum_lists

class TestSumLists(unittest.TestCase):
    def setUp(self):
        self.list1 = SinglyLinkedList()
        self.list1.add_to_tail(7)
        self.list1.add_to_tail(1)
        self.list1.add_to_tail(6)

        self.list2 = SinglyLinkedList()
        self.list2.add_to_tail(5)
        self.list2.add_to_tail(9)
        self.list2.add_to_tail(2)

        self.list3 = SinglyLinkedList()
        self.list3.add_to_tail(1)
        self.list3.add_to_tail(0)
    
    def test_sum_lists(self):
        self.assertEqual(self.print_list(sum_lists(self.list1, self.list2)), "2-1-9")
        self.assertEqual(self.print_list(sum_lists(self.list1, self.list3)), "8-1-6")

    def print_list(self, list):
        result = ""
        current = list.head
        while current:
            result += str(current.data) + "-"
            current = current.next
        return result[:-1]