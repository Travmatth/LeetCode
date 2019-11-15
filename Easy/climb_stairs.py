"""
You are climbing a stair case. It takes n steps to reach
to the top.
Each time you can either climb 1 or 2 steps. In how many
distinct ways can you climb to the top?
Note: Given n will be a positive integer.
"""

class Solution(object):
    def __init__(self):
        self.memo = {}

    def climbStairs_recursive_memoizatio(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.memo:
            return self.memo[n]
        elif n == 0:
            return 1
        elif n <= 0:
            return 0
        else:
            self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
            return self.memo[n]

    def climbStairs_dynamic_programming(self, n):
        """
        :type n: int
        :rtype: int
        """
        table = [(1 if not i or i == 1 else 0) for i in range(n + 1)]
        for i in range(2, n + 1):
            table[i] = table[i - 1] + table[i - 2]
        return table[n]

    def climbStairs(self, n):
        return self.climbStairs_dynamic_programming(n)

if __name__ == "__main__":
    s = Solution()
    ex_0 = s.climbStairs(2)
    if ex_0 != 2:
        print("ERROR")
    ex_1 = s.climbStairs(3)
    if ex_1 != 3:
        print("ERROR")
    ex_2 = s.climbStairs(6)
    if ex_2 != 13:
        print("ERROR")
    pass