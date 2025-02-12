import unittest
from Sort import algorithms


arrays = [
    [3, 7, 1, 0, 47, 1, 58, 74, 2, 5, 74],
    [9],
    [],
    [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

expected = [
    [0, 1, 1, 2, 3, 5, 7, 47, 58, 74, 74],
    [9],
    [],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
]


class AlgorithmsTests(unittest.TestCase):
    def test_bubble_sort(self):
        for i in range(len(arrays)):
            array = arrays[i]
            result = algorithms.bubble_sort(array)
            self.assertEqual(result, expected[i])

    def test_insertion_sort(self):
        for i in range(len(arrays)):
            array = arrays[i]
            result = algorithms.insertion_sort(array)
            self.assertEqual(result, expected[i])

    def test_merge_sort(self):
        for i in range(len(arrays)):
            array = arrays[i]
            result = algorithms.merge_sort(array)
            self.assertEqual(result, expected[i])

    def test_quick_sort(self):
        for i in range(len(arrays)):
            array = arrays[i]
            result = algorithms.quick_sort(array)
            self.assertEqual(result, expected[i])

    def test_counting_sort(self):
        for i in range(len(arrays)):
            array = arrays[i]
            result = algorithms.counting_sort(array)
            self.assertEqual(result, expected[i])


if __name__ == "__main__":
    unittest.main()
