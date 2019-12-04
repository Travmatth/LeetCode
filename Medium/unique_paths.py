"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach
the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?
note: m x n will be at most 100
"""

class Solution(object):
    def recursive_walk(self, m, n, y, x):
        """
        :type m: int
        :type n: int
        :type y: int
        :type x: int
        :rtype: int
        """
        if x + 1 == m and y + 1 == n:
            return 1
        elif x + 1 == m:
            return self.recursive_walk(m, n, y + 1, x)
        elif y + 1 == n:
            return self.recursive_walk(m, n, y, x + 1)
        else:
            return self.recursive_walk(m, n, y + 1, x) + self.recursive_walk(m, n, y, x + 1)

    def dynamic_walk(self, m, n):
        """
        :type m: int
        :type n: int
        :type y: int
        :type x: int
        :rtype: int
        """
        squares = [[0 for _ in range(m)] for _ in range(n)]
        for x in reversed(range(m)):
            for y in reversed(range(n)):
                if x + 1 == m and y + 1 == n:
                    squares[y][x] = 1
                elif x + 1 == m:
                    squares[y][x] = squares[y + 1][x]
                elif y + 1 == n:
                    squares[y][x] = squares[y][x + 1]
                else:
                    squares[y][x] = squares[y + 1][x] + squares[y][x + 1]
        return squares[0][0]

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # return self.recursive_walk(m, n, 0, 0)
        return self.dynamic_walk(m, n)

if __name__ == '__main__':
    s = Solution()
    ex_0 = s.uniquePaths(3, 2)
    if ex_0 != 3:
        print("Error")
    # top left -> bottom right there are three paths:
    # 1: r - r - d
    # 2: r - d - r
    # 3: d - r -  r
    ex_1 = s.uniquePaths(7, 3)
    if ex_1 != 28:
        print("Error")
    pass