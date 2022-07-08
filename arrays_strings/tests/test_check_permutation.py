import unittest
from check_permutation import check_permutation_sorted, check_permutation


class TestCheckPermutation(unittest.TestCase):
    def test_check_permutation_sorted(self):
        self.assertEqual(
            check_permutation_sorted(
                "abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz"
            ),
            True,
        )
        self.assertEqual(
            check_permutation_sorted(
                "abcdefghijklmnopqrstuvwxyz",
                "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",
            ),
            False,
        )
        self.assertEqual(check_permutation_sorted("", ""), True)
        self.assertEqual(check_permutation_sorted("a", "a"), True)
        self.assertEqual(check_permutation_sorted("aa", "aa"), True)
        self.assertEqual(check_permutation_sorted("ab", "ac"), False)
        self.assertEqual(check_permutation_sorted("hello", "olleh"), True)
        self.assertEqual(check_permutation_sorted("🐍", "🐍"), True)

    def test_check_permutation(self):
        self.assertEqual(
            check_permutation(
                "abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz"
            ),
            True,
        )
        self.assertEqual(
            check_permutation(
                "abcdefghijklmnopqrstuvwxyz",
                "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",
            ),
            False,
        )
        self.assertEqual(check_permutation("", ""), True)
        self.assertEqual(check_permutation("a", "a"), True)
        self.assertEqual(check_permutation("aa", "aa"), True)
        self.assertEqual(check_permutation("ab", "ac"), False)
        self.assertEqual(check_permutation("hello", "olleh"), True)
        self.assertEqual(check_permutation("🐍", "🐍"), True)
