"""
Given an integer n, return the number of trailing zeroes in n!.
Note: Your solution should be in logarithmic time complexity.
"""

class Solution(object):
    # https://brilliant.org/wiki/trailing-number-of-zeros/
    # f(x) = number of trailing zeroes in n!
    # f(x) = n/5 + n/(5^2) + n/(5^3) + ... + n/(5^k)
    # where n = log_5 k
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        magnitude = 5
        trailing = 0
        cur = n // magnitude
        while cur > 0:
            trailing += cur
            magnitude *= 5
            cur = n // magnitude
        return trailing

if __name__ == "__main__":
    s = Solution()
    ex_0 = s.trailingZeroes(3)
    if ex_0 != 0: #3! = 6, no trailing zero.
        print("Error")
    ex_1 = s.trailingZeroes(5)
    if ex_1 != 1: # 5! = 120, one trailing zero.
        print("Error")
    ex_2 = s.trailingZeroes(10005)
    # = 10005/5 + 10005/5 + 10005/125 + 10005/625 + 10005/3215
    # = 2001 + 400 + 80 + 16 + 3
    # = 25000
    if ex_2 != 2500:
        print("Error")
    pass