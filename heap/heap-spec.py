import unittest
from heap import Heap

class HeapTest(unittest.TestCase):
    def test_heap_min_insertion_1(self):
        heap = Heap('min')
        self.assertEqual(heap.insert(3), [3])
        self.assertEqual(heap.insert(2), [2, 3])
        self.assertEqual(heap.insert(1), [1, 3, 2])
        self.assertEqual(heap.insert(5), [1, 3, 2, 5])
        self.assertEqual(heap.extract(), (1, [2, 3, 5]))

    def test_heap_min_insertion_2(self):
        heap = Heap('min')
        self.assertEqual(heap.insert(9), [9])
        self.assertEqual(heap.insert(9), [9, 9])
        self.assertEqual(heap.insert(3), [3, 9, 9])
        self.assertEqual(heap.insert(4), [3, 4, 9, 9])
        self.assertEqual(heap.extract(), (3, [4, 9, 9]))
        self.assertEqual(heap.insert(5), [4, 5, 9, 9])
        self.assertEqual(heap.insert(6), [4, 5, 9, 9, 6])

    def test_heap_max_insertion(self):
        heap = Heap('max')
        self.assertEqual(heap.insert(7), [7])
        self.assertEqual(heap.insert(2), [7, 2])
        self.assertEqual(heap.insert(3), [7, 2, 3])
        self.assertEqual(heap.insert(1), [7, 2, 3, 1])
        self.assertEqual(heap.extract(), (7, [3, 2, 1]))
        

if __name__ == '__main__':
    unittest.main()