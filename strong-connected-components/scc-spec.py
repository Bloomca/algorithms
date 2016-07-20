import unittest
import scc

class SCCTest(unittest.TestCase):

    def test_scc_1(self):
        graph_array = [
            "1 4",
            "2 8",
            "3 6",
            "4 7",
            "5 2",
            "6 9",
            "7 1",
            "8 5",
            "8 6",
            "9 7",
            "9 3"
        ]

        sorted_sizes = sorted(scc.compute_scc(graph_array))
        self.assertEqual(sorted_sizes, [3, 3, 3])

    def test_scc_2(self):
        graph_array = [
            "1 2",
            "2 6",
            "2 3",
            "2 4",
            "3 1",
            "3 4",
            "4 5",
            "5 4",
            "6 5",
            "6 7",
            "7 6",
            "7 8",
            "8 5",
            "8 7"
        ]

        sorted_sizes = sorted(scc.compute_scc(graph_array))
        self.assertEqual(sorted_sizes, [2, 3, 3])

    def test_scc_3(self):
        graph_array = [
            "1 2",
            "2 3",
            "3 1",
            "3 4",
            "5 4",
            "6 4",
            "8 6",
            "6 7",
            "7 8"
        ]

        sorted_sizes = sorted(scc.compute_scc(graph_array))
        self.assertEqual(sorted_sizes, [1, 1, 3, 3])

    def test_scc_4(self):
        graph_array = [
            "1 2",
            "2 3",
            "3 1",
            "3 4",
            "5 4",
            "6 4",
            "8 6",
            "6 7",
            "7 8",
            "4 3",
            "4 6"
        ]

        sorted_sizes = sorted(scc.compute_scc(graph_array))
        self.assertEqual(sorted_sizes, [1, 7])

    def test_scc_5(self):
        graph_array = [
            "1 2",
            "2 3",
            "2 4",
            "2 5",
            "3 6",
            "4 5",
            "4 7",
            "5 2",
            "5 6",
            "5 7",
            "6 3",
            "6 8",
            "7 8",
            "7 10",
            "8 7",
            "9 7",
            "10 9",
            "10 11",
            "11 12",
            "12 10"
        ]

        sorted_sizes = sorted(scc.compute_scc(graph_array))
        self.assertEqual(sorted_sizes, [1, 2, 3, 6])

if __name__ == '__main__':
    unittest.main()