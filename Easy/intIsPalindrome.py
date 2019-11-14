class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x == 0:
            return True
        num = x
        val = 0
        while num:
            next = num % 10
            val = (val * 10) + next
            num /= 10
        return val == x

if __name__ == '__main__':
    s = Solution()
    ex_0 = s.isPalindrome(121) #true
    ex_1 = s.isPalindrome(-121) #false
    ex_2 = s.isPalindrome(12121) #true
    ex_3 = s.isPalindrome(12123) #false

