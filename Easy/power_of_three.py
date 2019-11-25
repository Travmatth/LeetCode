"""
Given an integer, write a function to determine if it is a power of three.
Follow up:
Could you do it without using any loop / recursion?
"""

class Solution(object):
	def isPowerOfThree(self, n):
		"""
		:type n: int
		:rtype: bool
		"""
		if not n:
			return False
		while not n % 3:
			n /= 3
		return True if n == 1 else False

if __name__ == "__main__":
	s = Solution()
	ex_0 = s.isPowerOfThree(27)
	if ex_0 != True:
		print("ERROR")
	ex_1 = s.isPowerOfThree(0)
	if ex_1 != False:
		print("ERROR")
	ex_2 = s.isPowerOfThree(9)
	if ex_2 != True:
		print("ERROR")
	ex_3 = s.isPowerOfThree(45)
	if ex_3 != False:
		print("ERROR")
	ex_4 = s.isPowerOfThree(1)
	if ex_4 != True:
		print("ERROR")
	pass