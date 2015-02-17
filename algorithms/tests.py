#!/usr/bin/env python
import unittest
import merge_sort
import threesum

class TestAlgo(unittest.TestCase):
    def test_merge_single_digit(self):
        numbers = [5,4,1,8,7,2,6,3]
        correct = [1,2,3,4,5,6,7,8]
        self.assertEqual(correct, merge_sort.merge_sort(numbers))

    def test_merge_double_digit(self):
        numbers = [5,9,12,3,1,53,193,6]
        correct = [1,3,5,6,9,12,53,193]
        self.assertEqual(correct, merge_sort.merge_sort(numbers))

#    def test_merge_odd(self):
#        numbers = [5,103,2,5,5,9,12,3,1,53,193,6]
#        correct = [1,2,3,5,5,5,6,9,12,53,103,193]
#        self.assertEqual(correct, merge_sort(numbers))

    def test_count_inversions_brute(self):
        array = [8,7,6,5,4,3,2,1]
        correct = 28
        self.assertEqual(merge_sort.count_inversions_brute(array), correct)

    def test_count_inversions(self):
        array = [8,7,6,5,4,3,2,1]
        correct = 28
        self.assertEqual(merge_sort.count_inversions(array)[1], correct)
        array = [8,7,6,5]
        correct = 6
        self.assertEqual(merge_sort.count_inversions(array)[1], correct)
        array = [8,7,6,5,3]
        correct = 10
        self.assertEqual(merge_sort.count_inversions(array)[1], correct)

    def test_three_sum_brute(self):
        array = [30,-40,-20,-10,40,0,10,5]
        self.assertEqual(threesum.three_sum_brute(array), 4)

#    def test_three_sum(self):
#        array = [30,-40,-20,-10,40,0,10,5]
#        self.assertEqual(threesum.three_sum(array), 4)

if __name__=='__main__': unittest.main()
