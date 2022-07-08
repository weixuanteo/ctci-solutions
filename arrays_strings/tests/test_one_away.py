import unittest
from one_away import is_one_away


class TestOneAway(unittest.TestCase):
    def test_is_one_away(self):
        self.assertEqual(is_one_away("pale", "ple"), True)
        self.assertEqual(is_one_away("pales", "pale"), True)
        self.assertEqual(is_one_away("pale", "bale"), True)
        self.assertEqual(is_one_away("pale", "bake"), False)
        self.assertEqual(is_one_away("bake", "bakes"), True)
        self.assertEqual(is_one_away("bake", "bake"), True)
        self.assertEqual(is_one_away("bake", "bkk"), False)
