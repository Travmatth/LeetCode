"""
Given two integers dividend and divisor, divide two integers
without using multiplication, division and mod operator.
Return the quotient after dividing dividend by divisor.
The integer division should truncate toward zero.
Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only
store integers within the 32-bit signed integer range:
[−231,  231 − 1]. For the purpose of this problem,
assume that your function returns 231 − 1 when the division
result overflows.
"""

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        count, quotient = 1, 0
        int_min, int_max = -(1 << 31), (1 << 31) - 1
        sign = False if (dividend >> 31) == (divisor >> 31) else True
        dividend, divisor = abs(dividend), abs(divisor)
        while dividend >= divisor:
            tmp = divisor
            m = 1
            # find max # which is multiple of divisor
            while (tmp << 1) <= dividend:
                tmp <<= 1
                m <<= 1
            dividend -= tmp
            quotient += m
        if (sign and -quotient < int_min):
            return int_min
        elif (not sign and quotient > int_max):
            return int_max
        return -quotient if sign else quotient
        

if __name__ == "__main__":
    s = Solution()
    ex_0 = s.divide(10, 3)
    if ex_0 != 3:
        print("Error")
    ex_1 = s.divide(7, -3)
    if ex_1 != -2:
        print("Error")
    ex_2 = s.divide(7, -3)
    if ex_2 != -2:
        print("Error")
    pass