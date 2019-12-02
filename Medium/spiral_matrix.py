"""
Given a matrix of m x n elements (m rows, n columns),
return all elements of the matrix in spiral order.
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        out = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        while left < right and top < bottom:
            # l -> r on top
            for i in range(left, right):
                out.append(matrix[top][i])
            top += 1
            # t -> b on right
            for i in range(top, bottom):
                out.append(matrix[i][right - 1])
            right -= 1
            # r -> l on bottom
            if top < bottom:
                for i in reversed(range(left, right)):
                    out.append(matrix[bottom - 1][i])
                bottom -= 1
            # b -> t on left
            if left < right:
                for i in reversed(range(top, bottom)):
                    out.append(matrix[i][left])
                left += 1
        return out

if __name__ == "__main__":
    s = Solution()
    ex_0 = s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    if ex_0 != [1, 2, 3, 6, 9, 8, 7, 4, 5]:
        print("Error")
    ex_1 = s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    if ex_1 != [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]:
        print("Error")
    pass