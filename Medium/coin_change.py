"""
You are given coins of different denominations and a total amount of
money amount. Write a function to compute the fewest number of coins
that you need to make up that amount. If that amount of money cannot
be made up by any combination of the coins, return -1.
Note:
You may assume that you have an infinite number of each kind of coin.
"""

from math import inf
from typing import *

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return 0
        dp = [0 if i == 0 else inf for i in range(amount + 1)]
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i - coin] + 1, dp[i])
        fewest = dp[amount]
        return fewest if fewest != inf else -1

if __name__ == "__main__":
    s = Solution()
    # Explanation: 11 = 5 + 5 + 1
    if s.coinChange([1, 2, 5], 11) != 3:
        print("error")
    if s.coinChange([2], 3) != -1:
        print("error")
    pass