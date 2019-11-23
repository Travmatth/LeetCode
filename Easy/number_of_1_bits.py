"""
Write a function that takes an unsigned integer and return the
number of '1' bits it has (also known as the Hamming weight).
Note:
Note that in some languages such as Java, there is no unsigned
integer type. In this case, the input will be given as signed
integer type and should not affect your implementation, as the
internal binary representation of the integer is the same
whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's
complement notation. Therefore, in Example 3 above the input
represents the signed integer -3.
Follow up:
If this function is called many times, how would you optimize it?
"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum = 0
        while n:
            sum += 1 if (n & 0x1) else 0
            n >>= 1
        return sum

if __name__ == "__main__":
    s = Solution()
    ex_0 = s.hammingWeight(11)
    if ex_0 != 3:
        print("ERROR")
    ex_1 = s.hammingWeight(2048)
    if ex_1 != 1:
        print("ERROR")
    ex_2 = s.hammingWeight(2048)
    if ex_2 != 1:
        print("ERROR")
    ex_3 = s.hammingWeight(2047)
    if ex_3 != 11:
        print("ERROR")
    pass