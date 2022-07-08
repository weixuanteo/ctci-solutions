import unittest

from string_rotation import is_string_rotation


class TestStringRotation(unittest.TestCase):
    def test_is_string_rotation(self):
        self.assertEqual(is_string_rotation("waterbottle", "erbottlewat"), True)
        self.assertEqual(is_string_rotation("waterbottle", "erbottlewaa"), False)
        self.assertEqual(is_string_rotation("waterbottle", "erbottlewa"), False)
