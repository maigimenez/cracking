import unittest
from random import randint, choice
from chapter_01.src.answer_08 import zero_matix


class TestZeroMatrix(unittest.TestCase):
    def test_zero_matrix(self):
        # N = randint(3, 10)
        # M = randint(3, 10)
        # # mat = []
        # for i in range(N):
        #     mat.append([])
        #     for j in range(M):
        #         value = randint(0, 10)
        #         mat[i].append(value)

        mat = [[0, 1, 2, 3], [1, 2, 3, 0], [1, 2, 3, 4], [1, 2, 3, 4]]
        zero_mat = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 2, 3, 0], [0, 2, 3, 0]]
        self.assertIs(zero_matix(mat), zero_mat)

        mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 0, 15, 16]]
        zero_mat = [[1, 0, 3, 4], [5, 0, 7, 8], [9, 0, 11, 10], [0, 0, 0, 0]]
        self.assertIs(zero_matix(mat), zero_mat)

        mat = [[1, 2, 3, 4, 0], [0, 7, 8, 9, 10], [11, 0, 13, 0, 15], [16, 17, 0, 19, 20]]
        mat = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        self.assertIs(zero_matix(mat), zero_mat)


    def test_is_empty(self):
        self.assertIs(zero_matix([]), False)

    def test_is_none(self):
        self.assertIs(zero_matix(None), False)


if __name__ == '__main__':
    unittest.main()