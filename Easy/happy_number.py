"""
Write an algorithm to determine if a number is "happy".
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the
sum of the squares of its digits, and repeat the process until
the number equals 1 (where it will stay), or it loops endlessly
in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if not n:
            return False
        seen = {}
        while n != 1:
            if n in seen:
                return False
            seen[n] = True
            nums = []
            while n != 0:
                nums.insert(0, n % 10)
                n //= 10
            nums = [n * n for n in nums]
            for num in nums:
                n += num
        return True

if __name__ == "__main__":
    s = Solution()
    ex_0 = s.isHappy(19)
    # Explanation: 
    # 12 + 92 = 82
    # 82 + 22 = 68
    # 62 + 82 = 100
    # 12 + 02 + 02 = 1
    if ex_0 != True:
        print("ERROR")
    ex_1 = s.isHappy(17)
    # Explanation: 
    # 12 + 92 = 82
    # 82 + 22 = 68
    # 62 + 82 = 100
    # 12 + 02 + 02 = 1
    if ex_1 != False:
        print("ERROR")