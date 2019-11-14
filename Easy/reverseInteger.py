class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        x *= sign
        val = 0
        while x:
            next = x % 10
            x /= 10
            val = (val * 10) + next
            if abs(val) > (1 << 31) - 1:
                return 0
        return sign * val

if __name__ == '__main__':
    s = Solution()
    ex_0 = s.reverse(123) #321
    ex_1 = s.reverse(-123) #-321
    ex_2 = s.reverse(120) #21
    ex_3 = s.reverse(1563847412) #0
