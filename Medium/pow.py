"""
Implement pow(x, n), which calculates x raised to the power n (xn).
Note:
    -100.0 < x < 100.0
    n is a 32-bit signed integer, within the range [−231, 231 − 1]
"""

class Solution(object):
	def myPow(self, x, n):
		"""
		:type x: float
		:type n: int
		:rtype: float
		"""
		if n == 0:
			return 1
		elif x in [0, 1] or n == 1:
			return x
		elif n == -1:
			return 1 / x
		half = self.myPow(x, n // 2 if n > 0 else (n+1) //2 )
		if n%2 == 0:
			return half * half
		elif n > 0:
			return half * half * x
		else:
			return half * half / x

if __name__ == "__main__":
	s = Solution()
	ex_0 = s.myPow(10, 0)
	if ex_0 != 1:
		print("Error")
	ex_1 = s.myPow(2.00000, 10)
	if ex_1 != 1024.00000:
		print("Error")
	ex_2 = s.myPow(2.10000, 3)
	if ex_2 != 9.26100:
		print("Error")
	ex_3 = s.myPow(2.00000, -2)
	if ex_3 != 0.25000:
		print("Error")
	pass