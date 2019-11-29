"""
Given an array nums, write a function to move all 0's to the end of it while
maintaining the relative order of the non-zero elements.
Note:
    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.
"""

class Solution(object):
	def moveZeroes(self, nums):
		"""
		:type nums: List[int]
		:rtype: None Do not return anything, modify nums in-place instead.
		"""
		i, n = len(nums) - 1, len(nums)
		while i >= 0:
			if i + 1 != n and not nums[i] and nums[i + 1]:
				nums[i], nums[i + 1] = nums[i + 1], nums[i]
				i += 1 if i != n else 0
			else:
				i -= 1

if __name__ == "__main__":
	s = Solution()
	ex_0 = s.moveZeroes([0,1,0,3,12])
	if ex_0 != [1,3,12,0,0]:
		print("ERROR")
	pass
