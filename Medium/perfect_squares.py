"""
Given a positive integer n, find the least number of perfect
square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
"""

import math

class Solution(object):
    def top_down_dp(self, n, x):
        if not n:
            return 0
        elif x * x > n:
            return math.inf
        inclusive = self.top_down_dp(n - (x * x), 1) + 1
        exclusive = self.top_down_dp(n, x + 1)
        return min(inclusive, exclusive)

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.top_down_dp(n, 1)

if __name__ == "__main__":
    s = Solution()
    # ex_0 = s.numSquares(12)
    # if ex_0 != 3:
    #     print("Error")
    # Explanation: 12 = 4 + 4 + 4.
    ex_1 = s.numSquares(13)
    if ex_1 != 2:
        print("Error")
    # Explanation: 13 = 4 + 9.
    pass