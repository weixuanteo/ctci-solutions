import unittest
from is_unique import is_unique, is_unique_chars

class TestIsUnique(unittest.TestCase):
    def test_is_unique(self):
        self.assertEqual(is_unique("abcdefghijklmnopqrstuvwxyz"), True)
        self.assertEqual(is_unique("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"), False)
        self.assertEqual(is_unique(""), True)
        self.assertEqual(is_unique("a"), True)
        self.assertEqual(is_unique("aa"), False)
        self.assertEqual(is_unique("ab"), True)
        self.assertEqual(is_unique("🐍"), True)
        self.assertEqual(is_unique("🐍🐍"), False)

    def test_is_unique_chars(self):
        self.assertEqual(is_unique_chars("abcdefghijklmnopqrstuvwxyz"), True)
        self.assertEqual(is_unique_chars("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"), False)
        self.assertEqual(is_unique_chars(""), True)
        self.assertEqual(is_unique_chars("a"), True)
        self.assertEqual(is_unique_chars("aa"), False)
        self.assertEqual(is_unique_chars("ab"), True)

if __name__ == '__main__':
    unittest.main()