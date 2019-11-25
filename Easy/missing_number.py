"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find
the one that is missing from the array.
Note:
Your algorithm should run in linear runtime complexity. Could you implement it
using only constant extra space complexity?
"""

class Solution(object):
	def missingNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		total, sum, i = 0, 0, 1
		for num in nums:
			total += i
			i += 1
			sum += num
		return total - sum

if __name__ == "__main__":
	s = Solution()
	ex_0 = s.missingNumber([3,0,1])
	if ex_0 != 2:
		print("ERROR")
	ex_1 = s.missingNumber([9,6,4,2,3,5,7,0,1])
	if ex_1 != 8:
		print("ERROR")
	pass