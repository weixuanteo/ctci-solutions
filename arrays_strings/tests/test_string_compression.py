import unittest
from string_compression import compress_string

class TestStringCompression(unittest.TestCase):
    def test_compress_string(self):
        self.assertEqual(compress_string("aabcccccaaa"), "a2b1c5a3")
        self.assertEqual(compress_string("abcdef"), "abcdef")
        self.assertEqual(compress_string("aabbcc"), "aabbcc")
        self.assertEqual(compress_string("aabbccdd"), "aabbccdd")
        self.assertEqual(compress_string("aabbccddeeff"), "aabbccddeeff")
        self.assertEqual(compress_string("aaaaab"), "a5b1")
        self.assertEqual(compress_string("aaabc"), "aaabc")
        self.assertEqual(compress_string(""), "")
        self.assertEqual(compress_string("a"), "a")
