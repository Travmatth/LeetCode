"""
Given a column title as appear in an Excel sheet,
return its corresponding column number.
For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
"""

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        for char in s:
            num *= 26
            num += (ord(char) - ord("A")) + 1
        return num


if __name__ == "__main__":
    s = Solution()
    ex_0 = s.titleToNumber("A")
    if ex_0 != 1:
        print("Error")
    ex_1 = s.titleToNumber("AB")
    if ex_1 != 28:
        print("Error")
    ex_2 = s.titleToNumber("ZY")
    if ex_2 != 701:
        print("Error")
    pass