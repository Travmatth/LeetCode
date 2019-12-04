"""
Given an m x n matrix, if an element is 0, set its
entire row and column to 0. Do it in place
"""

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None, modify matrix in place
        """
        cols, rows = len(matrix), len(matrix[0])
        col_zero, row_zero = False, False

        # check first row for zeroes
        for x in range(rows):
            if not matrix[0][x]:
                row_zero = True
                break
        # check first column for zeroes
        for y in range(cols):
            if not matrix[y][0]:
                col_zero = True
                break
        # check rest of matrix
        for y in range(1, cols):
            for x in range(1, rows):
                if not matrix[y][x]:
                    matrix[y][0], matrix[0][x] = 0, 0
        # set corresponding row and col as zero
        for y in range(1, cols):
            for x in range(1, rows):
                if not matrix[y][0] or not matrix[0][x]:
                    matrix[y][x] = 0
        if row_zero:
            for x in range(rows):
                matrix[0][x] = 0
        if col_zero:
            for y in range(cols):
                matrix[y][0] = 0

if __name__ == "__main__":
    s = Solution()
    m_0 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    s.setZeroes(m_0)
    if m_0 != [[1, 0, 1], [0, 0, 0], [1, 0, 1]]:
        print("Error")
    m_1 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    s.setZeroes(m_1)
    if m_1 != [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]:
        print("Error")
    m_2 = [[1, 1, 1], [0, 1, 2]]
    s.setZeroes(m_2)
    if m_2 != [[0, 1, 1], [0, 0, 0]]:
        print("Error")
    pass