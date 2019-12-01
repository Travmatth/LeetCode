"""
Calculate the sum of two integers a and b, but you are not
allowed to use the operator + and -.
"""

# 1.Why carry is a&b:
# If a and b are both 1 at the same digit, it creates one carry.
# Because you can only use 0 and 1 in binary, if you add 1+1 together, it will
# roll that over to the next digit, and the value will be 0 at this digit.
# if they are both 0 or only one is 1, it doesn't need to carry.
# Use ^ operation between a and b to find the different bit
# In my understanding, using ^ operator is kind of adding a and b together
# (a+b) but ignore the digit that a and b are both 1,
# because we already took care of this in step1.	

class Solution(object):
	def getSum(self, a, b):
		"""
		:type a: int
		:type b: int
		:rtype: int
		"""
		carry = 0
		mask = 0xffffffff
		while b & mask != 0:
			carry = (a & b) << 1
			a = a ^ b
			b = carry
		# for overflow condition like
		# -1
		#  1
		return a & mask if b > mask else a

if __name__ == "__main__":
	s = Solution()
	ex_0 = s.getSum(1, 2)
	if ex_0 != 3:
		print("ERROR")
	ex_1 = s.getSum(-2, 3)
	if ex_1 != 1:
		print("ERROR")
	pass