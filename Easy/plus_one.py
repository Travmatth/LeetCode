"""
Given a non-empty array of digits representing a non-negative
integer, plus one to the integer.
The digits are stored such that the most significant digit is at
the head of the list, and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except
the number 0 itself.
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                digits[i] += 1
            digits[i] += carry
            if digits[i] >= 10:
                carry = 1
                digits[i] %= 10
            else:
                carry = 0
        if carry:
            digits.insert(0, carry)
        return digits

if __name__ == "__main__":
    s = Solution()
    ex_1 = s.plusOne([1,2,3])
    if ex_1 != [1, 2, 4]:
        print("ERROR")
    ex_2 = s.plusOne([4,3,2,1])
    if ex_2 != [4,3,2,2]:
        print("ERROR")
    ex_3 = s.plusOne([9])
    if ex_3 != [1, 0]:
        print("ERROR")
    ex_4 = s.plusOne([1, 9])
    if ex_4 != [2, 0]:
        print("ERROR")
    ex_4 = s.plusOne([1, 1, 9])
    if ex_4 != [1, 2, 0]:
        print("ERROR")
