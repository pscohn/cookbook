#!/usr/bin/env python3
import unittest
import sort

class TestSort(unittest.TestCase):
    def test_swap(self):
        numbers = [1, 2, 3, 4, 5, 6]
        numbers = sort.swap(numbers, 1, 3)
        self.assertEqual(numbers, [1, 4, 3, 2, 5, 6])

    def test_selection(self):
        numbers = [4, 3, 8, 5, 9, 1, 2, 7, 0, 6]
        numbers = sort.selection(numbers)
        self.assertEqual(numbers, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

if __name__ == '__main__':
    unittest.main()

