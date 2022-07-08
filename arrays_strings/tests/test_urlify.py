import unittest

from urlify import urlify


class TestURLify(unittest.TestCase):
    def test_urlify(self):
        self.assertEqual(urlify("Mr John Smith    ", 13), "Mr%20John%20Smith")
