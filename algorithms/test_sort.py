#!/usr/bin/env python3
import unittest
import sort

class TestSort(unittest.TestCase):
    def setUp(self):
        self.numbers = [4, 3, 8, 5, 9, 1, 2, 7, 0, 6]
        self.correct = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_swap(self):
        numbers = [1, 2, 3, 4, 5, 6]
        numbers = sort.swap(numbers, 1, 3)
        self.assertEqual(numbers, [1, 4, 3, 2, 5, 6])

    def test_selection(self):
        self.assertEqual(sort.selection(self.numbers), self.correct)

    def test_insertion(self):
        self.assertEqual(sort.insertion(self.numbers), self.correct)

    def test_shell(self):
        self.assertEqual(sort.insertion(self.numbers, width=7), [4, 0, 6, 5, 9, 1, 2, 7, 3, 8])
#        self.assertEqual(sort.shell(self.numbers), self.correct)

if __name__ == '__main__':
    unittest.main()

