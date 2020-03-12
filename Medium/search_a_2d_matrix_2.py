"""
Write an efficient algorithm that searches for a value
in an m x n matrix. This matrix has the following properties:
Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
"""

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        rows, cols = len(matrix) - 1, len(matrix[0]) - 1
        y, x = 0, cols
        while True:
            if matrix[y][x] == target:
                return True
            elif y == cols and x == rows:
                return False
            elif target > matrix[y][x] and x == cols:
                y += 1
            else:
                x = (x + 1) % (cols + 1)

if __name__ == "__main__":
    s = Solution()
    matrix = [[1,   4,  7, 11, 15], [2,   5,  8, 12, 19], [3,   6,  9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    ex_0 = s.searchMatrix(matrix, 5)
    if ex_0 != True:
        print("Error")
    ex_1 = s.searchMatrix(matrix, 20)
    if ex_1 != True:
        print("Error")
    pass
