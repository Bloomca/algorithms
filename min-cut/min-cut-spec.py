import unittest
import min_cut

class MinCutTest(unittest.TestCase):

    def test_min_cut_1(self):
        graph_array = [
            "1 2 3 4 7",
            "2 1 3 4",
            "3 1 2 4",
            "4 1 2 3 5",
            "5 4 6 7 8",
            "6 5 7 8",
            "7 1 5 6 8",
            "8 5 6 7"
        ]

        min_cuts = min_cut.findMinCuts(graph_array)
        self.assertEqual(min_cuts, 2)

    def test_min_cut_2(self):
        graph_array = [
            "1 4 2 7 3",
            "2 4 1 3",
            "3 1 2 4",
            "4 5 1 2 3",
            "5 8 7 6 4",
            "6 8 5 7",
            "7 6 8 5 1",
            "8 7 6 5"
        ]

        min_cuts = min_cut.findMinCuts(graph_array)
        self.assertEqual(min_cuts, 2)

    def test_min_cut_3(self):
        graph_array = [
            "1 2 3 4",
            "2 1 3 4",
            "3 1 2 4",
            "4 1 2 3 5",
            "5 4 6 7 8",
            "6 5 7 8",
            "7 5 6 8",
            "8 5 6 7"
        ]

        min_cuts = min_cut.findMinCuts(graph_array)
        self.assertEqual(min_cuts, 1)

    def test_min_cut_4(self):
        graph_array = [
            "1 3 4 2",
            "2 1 4 3",
            "3 1 2 4",
            "4 5 3 2 1",
            "5 4 8 6 7",
            "6 8 7 5",
            "7 5 8 6",
            "8 5 7 6"
        ]

        min_cuts = min_cut.findMinCuts(graph_array)
        self.assertEqual(min_cuts, 1)

    def test_min_cut_5(self):
        graph_array = [
            "1 19 15 36 23 18 39",
            "2 36 23 4 18 26 9",
            "3 35 6 16 11",
            "4 23 2 18 24",
            "5 14 8 29 21",
            "6 34 35 3 16",
            "7 30 33 38 28",
            "8 12 14 5 29 31",
            "9 39 13 20 10 17 2",
            "10 9 20 12 14 29",
            "11 3 16 30 33 26",
            "12 20 10 14 8",
            "13 24 39 9 20",
            "14 10 12 8 5",
            "15 26 19 1 36",
            "16 6 3 11 30 17 35 32",
            "17 38 28 32 40 9 16",
            "18 2 4 24 39 1",
            "19 27 26 15 1",
            "20 13 9 10 12",
            "21 5 29 25 37",
            "22 32 40 34 35",
            "23 1 36 2 4",
            "24 4 18 39 13",
            "25 29 21 37 31",
            "26 31 27 19 15 11 2",
            "27 37 31 26 19 29",
            "28 7 38 17 32",
            "29 8 5 21 25 10 27",
            "30 16 11 33 7 37",
            "31 25 37 27 26 8",
            "32 28 17 40 22 16",
            "33 11 30 7 38",
            "34 40 22 35 6",
            "35 22 34 6 3 16",
            "36 15 1 23 2",
            "37 21 25 31 27 30",
            "38 33 7 28 17 40",
            "39 18 24 13 9 1",
            "40 17 32 22 34 38"
        ]

        min_cuts = min_cut.findMinCuts(graph_array)
        self.assertEqual(min_cuts, 3)

if __name__ == '__main__':
    unittest.main()