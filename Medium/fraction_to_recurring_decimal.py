"""
Given two integers representing the numerator and
denominator of a fraction, return the fraction in string format.
If the fractional part is repeating, enclose the repeating
part in parentheses.
"""

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign = True if numerator < 0 or denominator < 0 else False
        number, rem = divmod(abs(numerator), abs(denominator))
        tail, seen = '', {}
        while rem:
            if rem in seen:
                break
            seen[rem] = len(tail)
            n, rem = divmod(rem * 10, abs(denominator))
            tail += str(n)
        result = "-" if sign else "" 
        result += str(number) + '.' 
        result += tail if rem <= 0 else tail[:seen[rem]] + '(' + tail[seen[rem]:] + ')'
        return result.rstrip('.')

if __name__ == "__main__":
    s = Solution()
    ex_0 = s.fractionToDecimal(1, 2)
    if ex_0 != "0.5":
        print("Error")
    ex_1 = s.fractionToDecimal(2, 1)
    if ex_1 != "2":
        print("Error")
    ex_2 = s.fractionToDecimal(2, 3)
    if ex_2 != "0.(6)":
        print("Error")
    pass