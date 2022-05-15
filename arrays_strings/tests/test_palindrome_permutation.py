import unittest
from palindrome_permutation import is_palindrome_permutation

class TestPalindromePermutation(unittest.TestCase):
    def test_is_palindrome_permutation(self):
        self.assertEqual(is_palindrome_permutation(""), True)
        self.assertEqual(is_palindrome_permutation("a"), True)
        self.assertEqual(is_palindrome_permutation("Tact Coa"), True)
        self.assertEqual(is_palindrome_permutation("Tact Coa "), True)
        self.assertEqual(is_palindrome_permutation("Hello"), False)
        self.assertEqual(is_palindrome_permutation("tactcoapapa"), True)
