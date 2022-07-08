import unittest

from singly_linked_list import SinglyLinkedList
from palindrome import is_palindrome


class TestIsPalindrome(unittest.TestCase):
    def setUp(self):
        self.list1 = SinglyLinkedList()
        self.list1.add_to_tail("h")
        self.list1.add_to_tail("e")
        self.list1.add_to_tail("l")
        self.list1.add_to_tail("l")
        self.list1.add_to_tail("o")

        self.list2 = SinglyLinkedList()
        self.list2.add_to_tail("a")
        self.list2.add_to_tail("a")
        self.list2.add_to_tail("b")
        self.list2.add_to_tail("a")
        self.list2.add_to_tail("a")

        self.list3 = SinglyLinkedList()

        self.list4 = SinglyLinkedList()
        self.list4.add_to_tail("a")

    def test_is_palindrome(self):
        self.assertFalse(is_palindrome(self.list1))
        self.assertTrue(is_palindrome(self.list2))
        self.assertTrue(is_palindrome(self.list3))
        self.assertTrue(is_palindrome(self.list4))
