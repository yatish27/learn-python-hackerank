#!/usr/bin/python3
import unittest
import max_xor

class MaxXorTestCase(unittest.TestCase):
    def test_max_xor(self):
        self.assertEqual(7, max_xor.max_xor(10, 15))
        self.assertEqual(15, max_xor.max_xor(1, 10))

if __name__ == '__main__':
    unittest.main()


