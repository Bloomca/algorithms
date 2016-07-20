import unittest
import dijkstra

class DijkstraTest(unittest.TestCase):

    def test_dijkstra_1(self):
        graph_array = [
            "1	2,1	8,2",
            "2	1,1	3,1",
            "3	2,1	4,1",
            "4	3,1	5,1",
            "5	4,1	6,1",
            "6	5,1	7,1",
            "7	6,1	8,1",
            "8	7,1	1,2"
        ]

        self.assertEqual(4, dijkstra.compute_paths(graph_array, 1, 5))
        self.assertEqual(4, dijkstra.compute_paths(graph_array, 1, 6))
        self.assertEqual(3, dijkstra.compute_paths(graph_array, 1, 7))
        self.assertEqual(2, dijkstra.compute_paths(graph_array, 1, 8))

    def test_dijkstra_2(self):
        graph_array = [
            "1 2,1 5,3 8,3",
            "2 1,1 3,4 7,2 8,1",
            "3 2,4 4,1 5,2 7,1 8,3",
            "4 3,1",
            "5 1,3 3,2 6,1 7,1",
            "6 5,1",
            "7 2,2 3,1 5,1 8,2",
            "8 1,3 2,1 3,3 7,2 9,1",
            "9 8,1 10,3 11,2",
            "10 9,3 11,3",
            "11 9,2 10,3"
        ]

        self.assertEqual(4, dijkstra.compute_paths(graph_array, 1, 3))
        self.assertEqual(5, dijkstra.compute_paths(graph_array, 1, 4))
        self.assertEqual(3, dijkstra.compute_paths(graph_array, 1, 5))
        self.assertEqual(4, dijkstra.compute_paths(graph_array, 1, 6))
        self.assertEqual(3, dijkstra.compute_paths(graph_array, 1, 7))
        self.assertEqual(2, dijkstra.compute_paths(graph_array, 1, 8))
        self.assertEqual(3, dijkstra.compute_paths(graph_array, 1, 9))
        self.assertEqual(6, dijkstra.compute_paths(graph_array, 1, 10))
        self.assertEqual(5, dijkstra.compute_paths(graph_array, 1, 11))

if __name__ == '__main__':
    unittest.main()