import unittest
import quicksort

class QuicksortTest(unittest.TestCase):
    """Tests for quicksort algorithm"""

    def test_sorting_correctness(self):
        """It should sort correctly despite pivot selection strategy"""
        unsorted_array = [3, 8, 2, 5, 1, 4, 7, 6]
        sorted_array_with_first, _ = quicksort.quicksort(unsorted_array, quicksort.select_first)
        sorted_array_with_last, _ = quicksort.quicksort(unsorted_array, quicksort.select_last)
        sorted_array_with_middle, _ = quicksort.quicksort(unsorted_array, quicksort.select_middle)
        self.assertEqual(sorted_array_with_first, [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(sorted_array_with_first, sorted_array_with_last)
        self.assertEqual(sorted_array_with_first, sorted_array_with_middle)

    def test_correct_sorting_duplicates(self):
        """It should treat same values correctly"""
        unsorted_array = [1, 5, 2, 20, 12, 14, 2, 5, 1]
        sorted_array, _ = quicksort.quicksort(unsorted_array, quicksort.select_middle)

        self.assertEqual(sorted_array, [1, 1, 2, 2, 5, 5, 12, 14, 20])

    def test_swap_checks_correctness(self):
        """It should calculcate swap checks correctly"""
        # because it is in decreasing order, we will check it 5 + 4 + 3 + 2 + 1 times
        unsorted_array = [6, 5, 4, 3, 2, 1]
        _, number_of_checks = quicksort.quicksort(unsorted_array, quicksort.select_first)

        self.assertEqual(number_of_checks, 15)

if __name__ == '__main__':
    unittest.main()