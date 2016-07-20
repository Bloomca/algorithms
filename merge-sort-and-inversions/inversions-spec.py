import unittest
import inversions

class InversionsTest(unittest.TestCase):

    def test_merging_correctness(self):
        array = [5, 2, 10, 2, 8, 1, 4]
        sorted_array, _ = inversions.mergeSort(array)
        
        self.assertEqual(sorted_array, [1, 2, 2, 4, 5, 8, 10])

    def test_inversions_1(self):
        array = [1,3,5,2,4,6]
        sorted_array, number_of_inversions = inversions.mergeSort(array)

        self.assertEqual(sorted_array, [1, 2, 3, 4, 5, 6])
        self.assertEqual(number_of_inversions, 3)

    def test_inversions_2(self):
        array = [1,5,3,2,4]
        sorted_array, number_of_inversions = inversions.mergeSort(array)

        self.assertEqual(sorted_array, [1, 2, 3, 4, 5])
        self.assertEqual(number_of_inversions, 4)

    def test_inversions_3(self):
        array = [5,4,3,2,1]
        sorted_array, number_of_inversions = inversions.mergeSort(array)

        self.assertEqual(sorted_array, [1, 2, 3, 4, 5])
        self.assertEqual(number_of_inversions, 10)

    def test_inversions_4(self):
        array = [1,6,3,2,4,5]
        sorted_array, number_of_inversions = inversions.mergeSort(array)

        self.assertEqual(sorted_array, [1, 2, 3, 4, 5, 6])
        self.assertEqual(number_of_inversions, 5)

    def test_inversions_5(self):
        array = [9, 12, 3, 1, 6, 8, 2, 5, 14, 13, 11, 7, 10, 4, 0]
        sorted_array, number_of_inversions = inversions.mergeSort(array)

        self.assertEqual(sorted_array, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
        self.assertEqual(number_of_inversions, 56)

    def test_inversions_6(self):
        array = [
            37, 7, 2, 14, 35, 47, 10, 24, 44, 17, 34, 11, 16, 48, 1, 39, 6, 33, 43, 26, 40, 4,
            28, 5, 38, 41, 42, 12, 13, 21, 29, 18, 3, 19, 0, 32, 46, 27, 31, 25, 15, 36, 20, 8,
            9, 49, 22, 23, 30, 45
        ]
        _, number_of_inversions = inversions.mergeSort(array)

        self.assertEqual(number_of_inversions, 590)

    def test_inversions_5(self):
        array = [
            4, 80, 70, 23, 9, 60, 68, 27, 66, 78, 12, 40, 52, 53, 44, 8, 49, 28, 18, 46, 21, 39, 51,
            7, 87, 99, 69, 62, 84, 6, 79, 67, 14, 98, 83, 0, 96, 5, 82, 10, 26, 48, 3, 2, 15, 92, 11,
            55, 63, 97, 43, 45, 81, 42, 95, 20, 25, 74, 24, 72, 91, 35, 86, 19, 75, 58, 71, 47, 76,
            59, 64, 93, 17, 50, 56, 94, 90, 89, 32, 37, 34, 65, 1, 73, 41, 36, 57, 77, 30, 22, 13,
            29, 38, 16, 88, 61, 31, 85, 33, 54
        ]
        _, number_of_inversions = inversions.mergeSort(array)

        self.assertEqual(number_of_inversions, 2372)
        

if __name__ == '__main__':
    unittest.main()