import selection_sort
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(selection_sort.sort([1]), [1])

    def test_case_2(self):
        self.assertEqual(selection_sort.sort([1, 2]), [1, 2])

    def test_case_3(self):
        self.assertEqual(selection_sort.sort([2, 1]), [1, 2])

    def test_case_4(self):
        self.assertEqual(selection_sort.sort([1, 3, 2]), [1, 2, 3])

    def test_case_5(self):
        self.assertEqual(selection_sort.sort([3, 1, 2]), [1, 2, 3])

    def test_case_6(self):
        self.assertEqual(selection_sort.sort([1, 2, 3]), [1, 2, 3])

    def test_case_7(self):
        self.assertEqual(
            selection_sort.sort(
                [-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7, -6, -7, 8,]
            ),
            [-10, -7, -7, -6, -6, -5, -5, -4, -4, -4, -2, -1, 1, 3, 5, 5, 6, 8, 8, 10],
        )

    def test_case_8(self):
        self.assertEqual(
            selection_sort.sort(
                [-7, 2, 3, 8, -10, 4, -6, -10, -2, -7, 10, 5, 2, 9, -9, -5, 3, 8]
            ),
            [-10, -10, -9, -7, -7, -6, -5, -2, 2, 2, 3, 3, 4, 5, 8, 8, 9, 10],
        )

    def test_case_9(self):
        self.assertEqual(
            selection_sort.sort(
                [ 8, -6, 7, 10, 8, -1, 6, 2, 4, -5, 1, 10, 8, -10, -9, -10, 8, 9, -2, 7, -2, 4,]
            ),
            [-10, -10, -9, -6, -5, -2, -2, -1, 1, 2, 4, 4, 6, 7, 7, 8, 8, 8, 8, 9, 10, 10,],
        )

    def test_case_10(self):
        self.assertEqual(
            selection_sort.sort([5, -2, 2, -8, 3, -10, -6, -1, 2, -2, 9, 1, 1]),
            [-10, -8, -6, -2, -2, -1, 1, 1, 2, 2, 3, 5, 9],
        )


if __name__ == "__main__":
    unittest.main()