import unittest
from singly_linked_list import SinglyLinkedList
from remove_dups import remove_dups

class TestRemoveDups(unittest.TestCase):
    def setUp(self):
        self.list1 = SinglyLinkedList()
        self.list1.add_to_head(1)
        self.list1.add_to_head(2)
        self.list1.add_to_head(3)
        self.list1.add_to_head(4)
        
        self.list2 = SinglyLinkedList()
        self.list2.add_to_tail(2)
        self.list2.add_to_tail(3)
        self.list2.add_to_tail(2)
        self.list2.add_to_tail(4)
        self.list2.add_to_tail(4)
        self.list2.add_to_tail(2)

        self.list3 = SinglyLinkedList()

        self.list4 = SinglyLinkedList()
        self.list4.add_to_head(1)
        self.list4.add_to_head(1)
        self.list4.add_to_head(1)
        self.list4.add_to_head(1)
        self.list4.add_to_head(1)


    def test_remove_dups(self):
        self.list1 = remove_dups(self.list1)
        self.assertEqual(self.print_list(self.list1), "4-3-2-1")
        self.list2 = remove_dups(self.list2)
        self.assertEqual(self.print_list(self.list2), "2-3-4")
        self.list3 = remove_dups(self.list3)
        self.assertEqual(self.print_list(self.list3), "")
        self.list4 = remove_dups(self.list4)
        self.assertEqual(self.print_list(self.list4), "1")

    def print_list(self, list) -> str:
        output = ""
        current = list.head
        while current:
            output += str(current.data) + "-"
            current = current.next
        return output[:-1]