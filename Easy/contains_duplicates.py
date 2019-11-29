"""
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the
array, and it should return false if every element is distinct.
"""

class Solution(object):
	def containsDuplicate(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		seen = {}
		for num in nums:
			if num in seen:
				return True
			seen[num] = True
		return False

if __name__ == "__main__":
	s = Solution()
	ex_0 = s.containsDuplicate([1,2,3,1])
	if ex_0 != True:
		print("error")
	ex_1 = s.containsDuplicate([1,2,3,4])
	if ex_1 != False:
		print("error")
	ex_2 = s.containsDuplicate([1,1,1,3,3,4,3,2,4,2])
	if ex_2 != True:
		print("error")
	pass