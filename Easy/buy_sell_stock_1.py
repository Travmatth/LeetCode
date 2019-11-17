"""
Say you have an array for which the ith element is the
price of a given stock on day i.
If you were only permitted to complete at most one transaction
(i.e., buy one and sell one share of the stock), design an
algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.
"""

class Solution(object):
    def maxMiddle(self, left, right, cur):
        max, l_cur, r_cur  = 0, left[-1], right[0]
        for i in reversed(left[:-1]):
            if i < l_cur:
                l_cur = i
        for i in right[1:]:
            if i >= r_cur:
                r_cur = i
        max = r_cur - l_cur
        return max if max > cur else cur

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0 or n == 1:
            return 0
        elif n == 2:
            diff = prices[1] - prices[0]
            return 0 if  diff < 0 else diff
        mid = n // 2
        left = self.maxProfit(prices[:mid])
        right = self.maxProfit(prices[mid:])
        max = left if left > right else right
        return self.maxMiddle(prices[:mid], prices[mid:], max)

if __name__ == "__main__":
    s = Solution()
    ex_0 = s.maxProfit([7,1,5,3,6,4])
    if ex_0 != 5:
        print("ERROR")
    ex_1 = s.maxProfit([7,6,4,3,1])
    if ex_1 != 0:
        print("ERROR")
    pass
