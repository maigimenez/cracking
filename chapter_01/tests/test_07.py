import unittest

from chapter_01.src.answer_07 import rotate_matrix


class TestRotateMatrix(unittest.TestCase):
    '''
    All these tests assume a clockwise rotation
    '''
    def test_size_zero(self):
        self.assertEqual(rotate_matrix([]), [])

    def test_size_one(self):
        self.assertEqual(rotate_matrix([[1]]), [[1]])

    def test_size_two(self):
        self.assertEqual(rotate_matrix([[1, 2], [3, 4]]),
                         [[3, 1], [4, 2]])

    def test_size_odd(self):
        self.assertEqual(rotate_matrix([[1,  3,  4, 10, 11],
                                        [2,  5,  9, 12, 19],
                                        [6,  8, 13, 18, 20],
                                        [7, 14, 17, 21, 24],
                                        [15, 16, 22, 23, 25]]),
                         [[15,  7,  6,  2,  1],
                          [16, 14,  8,  5,  3],
                          [22, 17, 13,  9,  4],
                          [23, 21, 18, 12, 10],
                          [25, 24, 20, 19, 11]])

    def test_size_even(self):
        self.assertEqual(rotate_matrix([[1,  4,  9, 16, 25, 36],
                                        [1,  3,  5,  7,  9, 11],
                                        [2,  7, 14, 23, 34, 47],
                                        [3,  5,  7,  9, 11, 13],
                                        [5, 12, 21, 32, 45, 60],
                                        [8,  7,  9, 11, 13, 15]]),
                         [[8,  5,  3,  2,  1,  1],
                          [7, 12,  5,  7,  3,  4],
                          [9, 21,  7, 14,  5,  9],
                          [11, 32,  9, 23,  7, 16],
                          [13, 45, 11, 34,  9, 25],
                          [15, 60, 13, 47, 11, 36]])

if __name__ == "__main__":
    unittest.main()
