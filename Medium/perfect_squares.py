"""
Given a positive integer n, find the least number of perfect square numbers
(for example, 1, 4, 9, 16, ...) which sum to n.
I had a hard time with this too. Let's take the example number n=13.
    First thing to observe is that: 1^2 =1, 2^2=4, 3^2=9, 4^2=16
        So 13 can't be composed of anything greater than 3^2. Generically
		speaking, n can only be composed of numbers 1 to sqrt(n)
        So we are left with some combination of the square of the following
		numbers: 1, 2, or 3.
    Next thing we want to do is come up with the recursive formula. This took
	me a long time to understand. But we basically want to dwindle down to work
	with a smaller n (that's the whole point of recursion). We do that by
	subtracting our candidate perfect squares from n. For example:
        If we try 3, then dp(13)=dp(13-3^2)+1=dp(4)+1. The +1 is incrementing
		the count by 1 and is from the the fact that we already took off a
		perfect square from 13, which was the 3^2. Each +1 is a perfect square
		that we took off.
        If we try 2, then dp(13)=13-2^2=dp(9)+1
        If we try 1, then dp(13)=13-1^2=dp(12)+1
So we are left with comparing which is the smallest out of dp(4), dp(9), and
dp(12). Hence the min.
"""

from math import inf, sqrt

class Solution(object):
	def top_down_dp(self, n, x):
		if not n:
			return 0
		elif x * x > n:
			return inf
		# if x belongs to smallest set of perfect squares
		inclusive = self.top_down_dp(n - (x * x), 1) + 1
		# if x does not belong to smallest set of perfect squares
		exclusive = self.top_down_dp(n, x + 1)
		return min(inclusive, exclusive)

	def top_down_dp_simple_memo(self, n, x, memo):
		if not n:
			return 0
		elif x * x > n:
			return inf
		elif memo[n][x] != None:
			return memo[n][x]
		# if x belongs to smallest set of perfect squares
		inclusive = self.top_down_dp_simple_memo(n - (x * x), 1, memo) + 1
		# if x does not belong to smallest set of perfect squares
		exclusive = self.top_down_dp_simple_memo(n, x + 1, memo)
		memo[n][x] = min(inclusive, exclusive)
		return memo[n][x]

	def top_down_dp(self, n, memo):
		if not n:
			return 0
		elif memo[n] != None:
			return memo[n]
		result = self.top_down_dp(n - 1, memo) + 1
		c = 2
		while c * c <= n:
			m = [None for _ in range(n + 1)]
			i = self.top_down_dp(n - (c * c), m) + 1
			result = min(result, i)
			c += 1
		memo[n] = result
		return result
 
	def bottom_up_dp(self, n):
		i, memo = 1, [0 for _ in range(n + 1)]
		while i <= n:
			memo[i] = memo[i - 1] + 1
			c = 2
			while c * c <= i:
				memo[i] = min(memo[i], memo[i - (c * c)] + 1)
				c += 1
			i += 1
		return memo[n]

	def numSquares(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		# return self.top_down_dp(n, 1)
		# memo = [[None for _ in range(int(sqrt(n)) + 1)] for _ in range(n + 1)]
		# return self.top_down_dp_simple_memo(n, 1, memo)
		# dp = [None for _ in range(n + 1)]
		# return self.top_down_dp(n, dp)
		return self.bottom_up_dp(n)

if __name__ == "__main__":
	s = Solution()
	ex_0 = s.numSquares(12)
	if ex_0 != 3:
		print("Error")
	# Explanation: 12 = 4 + 4 + 4.
	ex_1 = s.numSquares(13)
	if ex_1 != 2:
		print("Error")
	# Explanation: 13 = 4 + 9.
	pass