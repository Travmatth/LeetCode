"""
Implement int sqrt(int x).
Compute and return the square root of x, where
x is guaranteed to be a non-negative integer.
Since the return type is an integer, the decimal digits are
truncated and only the integer part of the result is returned.
"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        low = 0
        high = x // 2
        while low <= high:
            mid = (low + high) // 2
            square = mid * mid
            if square == x:
                return mid
            elif square < x:
                low = mid + 1
                ans = mid
            else:
                high = mid - 1
        return ans

if __name__ == "__main__":
    s = Solution()
    ex_0 = s.mySqrt(4) 
    if ex_0 != 2:
        print("ERROR")
    ex_1 = s.mySqrt(8)
    if ex_1 != 2:
        print("ERROR")
    ex_2 = s.mySqrt(9)
    if ex_2 != 3:
        print("ERROR")
    ex_3 = s.mySqrt(12)
    if ex_3 != 3:
        print("ERROR")