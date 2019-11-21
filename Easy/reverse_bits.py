"""
Reverse bits of a given 32 bits unsigned integer.
"""

class Solution:
    def reverseBits(self, n):
        # https://stackoverflow.com/questions/12681945/reversing-bits-of-python-integer
        # @param n, an integer
        # @return an integer
        reversed = 0
        for _ in range(32):
            reversed = (reversed << 1) + (n & 1)
            n >>= 1
        return reversed

if __name__ == "__main__":
    s = Solution()
    ex_2 = s.reverseBits(1)#11111111111111111111111111111101
    if ex_2 != 2147483648: #10111111111111111111111111111111
        print("error")
    ex_0 = s.reverseBits(43261596) #00000010 10010100 00011110 10011100
    if ex_0 != 964176192:          #00111001 01111000 00101001 01000000
        print("error")
    ex_1 = s.reverseBits(4294967293)#11111111111111111111111111111101
    if ex_1 != 3221225471: #10111111111111111111111111111111
        print("error")
    pass
    