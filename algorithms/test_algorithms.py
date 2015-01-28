#!/usr/bin/env python3
import unittest
from lonely_integer import lonely_integer

class TestAlgorithms(unittest.TestCase):
    def test_lonely_integer(self):
        array = [1,1,2,2,3,4,4,5,5]
        result = 3
        self.assertEqual(result, lonely_integer(array))




if __name__ == '__main__':
    unittest.main()

