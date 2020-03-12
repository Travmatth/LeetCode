"""
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions
as you like (ie, buy one and sell one share of the stock multiple times) with the
following restrictions:
You may not engage in multiple transactions at the same time (ie, you must sell the
stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
"""
from typing import *

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0
        n = len(prices)
        sales = [0 for _ in range(n)]
        cooldowns = [0 for _ in range(n)]
        i = 2
        sales[1] = prices[1] - prices[0]
        while i < n:
            cooldowns[i] = max(cooldowns[i - 1], sales[i - 1])
            sales[i] = prices[i] - prices[i - 1] + max(sales[i - 1], cooldowns[i - 2]) 
            i += 1
        return max(sales[n - 1], cooldowns[n - 1])

if __name__ == "__main__":
    s = Solution()
    if s.maxProfit([1,2,4]) != 3:
        print("Error") 
    if s.maxProfit([1,2]) != 1:
        print("Error") 
    # Explanation: transactions = [buy, sell, cooldown, buy, sell]
    if s.maxProfit([1,2,3,0,2]) != 3:
        print("Error") 
    pass