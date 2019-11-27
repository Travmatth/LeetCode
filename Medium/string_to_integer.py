"""
Implement atoi which converts a string to an integer.
The function first discards as many whitespace characters as necessary until the first
non-whitespace character is found. Then, starting from this character, takes an optional
initial plus or minus sign followed by as many numerical digits as possible, and interprets
them as a numerical value.
The string can contain additional characters after those that form the integral number,
which are ignored and have no effect on the behavior of this function.
If the first sequence of non-whitespace characters in str is not a valid integral number,
or if no such sequence exists because either str is empty or it contains only whitespace
characters, no conversion is performed.
If no valid conversion could be performed, a zero value is returned.
Note:
Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit
signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of
representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
"""

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        start, sign, sum = 0, False, 0
        while start < len(str) and not str[start].isdigit():
            if str[start] == ' ':
                start += 1
            elif str[start] == '+':
                start += 1
                break
            elif str[start] == '-':
                sign = True
                start += 1
                break
            else:
                return 0 
        base, int_min, int_max = ord('0'), (1 << 31), (1 << 31) - 1
        for num in str[start:]:
            if not num.isdigit():
                break
            next = ord(num) - base
            sum = (sum * 10) + next
            if sign and sum >= int_min:
                return -int_min 
            elif not sign and sum >= int_max:
                return int_max
        return sum if not sign else -sum

if __name__ == "__main__":
    s = Solution()
    ex_0 = s.myAtoi("42")
    if ex_0 != 42:
        print("Error")
    ex_1 = s.myAtoi("   -42")
    if ex_1 != -42:
        print("Error")
    # Explanation: The first non-whitespace character is '-', which is the minus sign.
    #  Then take as many numerical digits as possible, which gets 42.
    ex_2 = s.myAtoi("4193 with words")
    if ex_2 != 4193:
        print("Error")
    # Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
    ex_3 = s.myAtoi("words and 987")
    if ex_3 != 0:
        print("Error")
    # Explanation: The first non-whitespace character is 'w', which is not a numerical 
    #  digit or a +/- sign. Therefore no valid conversion could be performed.
    ex_4 = s.myAtoi("-91283472332")
    if ex_4 != -2147483648:
        print("Error")
    # Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
    # Thefore INT_MIN (−231) is returned.
    ex_5 = s.myAtoi(".1")
    if ex_5 != 0:
        print("Error")
    ex_6 = s.myAtoi(" ")
    if ex_6 != 0:
        print("Error")
    ex_7 = s.myAtoi("  -0012a42")
    if ex_7 != 0:
        print("Error")
    pass