"""
Say you have an array for which the ith element is the
price of a given stock on day i.
Design an algorithm to find the maximum profit. You may
complete as many transactions as you like (i.e., buy one
and sell one share of the stock multiple times).
Note: You may not engage in multiple transactions at the
same time (i.e., you must sell the stock before you buy again).
"""

class Solution(object):
    def maxProfit_greedy(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # the local max profit will result in the global max profit
        # seek out local ascending series
        if not prices:
            return 0
        n = len(prices)
        if not n:
            return 0
        max_profit, min_buy = 0, 0
        for i in range(n):
            if (prices[i] < prices[i - 1]):
                max_profit += prices[i - 1] - prices[min_buy]
                min_buy = i
        if prices[min_buy] < prices[n - 1]:
            max_profit += prices[n - 1] - prices[min_buy]
        return max_profit

    def maxProfit_dp (self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # http://buttercola.blogspot.com/2014/09/leetcode-best-time-to-buy-and-sell.html
        # define DP array where dp[i] is max profit at day i
        # initial state dp[0] means we buy and sell first day
        # transition fx: dp[i] = dp[i - 1] + prices[i] - prices[i - 1]
        #   where prices[i] <= prices[i - 1]
        # final state: check dp[n]
        pass



    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        pass

if __name__ == "__main__":
    s = Solution()
    ex_0 = s.maxProfit([7,1,5,3,6,4])
    if ex_0 != 7:
        print("ERROR")
    ex_1 = s.maxProfit([1,2,3,4,5])
    if ex_1 != 4:
        print("ERROR")
    pass
