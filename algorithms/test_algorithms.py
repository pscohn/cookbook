#!/usr/bin/env python3
import unittest
from lonely_integer import lonely_integer
from algorithms import *

class TestAlgorithms(unittest.TestCase):
    def test_lonely_integer(self):
        array = [1,1,2,2,3,4,4,5,5]
        result = 3
        self.assertEqual(result, lonely_integer(array))

    def test_binary_search(self):
        array = [1, 3, 4, 8, 23, 49, 482, 849]
        self.assertEqual(2, binary_search(array, 4, 0, len(array)))
        self.assertEqual(5, binary_search(array, 49, 0, len(array)))
        self.assertEqual(7, binary_search(array, 849, 0, len(array)))
        self.assertEqual(None, binary_search(array, 50, 0, len(array)))

if __name__ == '__main__':
    unittest.main()

