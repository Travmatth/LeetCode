"""
Given a 2D matrix matrix, find the sum of the elements inside
the rectangle defined by its upper left corner (row1, col1) and
lower right corner (row2, col2).
Range Sum Query 2D
The above rectangle (with the red border) is defined by
(row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.
Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.
"""

class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        total = 0
        for row in range(row1, row2 + 1):
            total += sum(self.matrix[row][col1: col2 + 1])
        return total

if __name__ == "__main__":
    # Your NumMatrix object will be instantiated and called as such:
    matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
    s = NumMatrix(matrix)
    ex_0 = s.sumRegion(2, 1, 4, 3)
    if ex_0 != 8:
        print("Error")
    ex_1 = s.sumRegion(1, 1, 2, 2)
    if ex_1 != 11:
        print("Error")
    ex_2 = s.sumRegion(1, 2, 2, 4)
    if ex_2 != 12:
        print("Error")
    pass