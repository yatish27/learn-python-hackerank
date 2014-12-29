#!/usr/bin/python3

import unittest
from utopian_tree import calculate_height
class UtopainTestCase(unittest.TestCase):
    def test_utopian_tree(self):
        self.assertEqual(6, calculate_height(3))

if __name__ == '__main__':
    unittest.main()
