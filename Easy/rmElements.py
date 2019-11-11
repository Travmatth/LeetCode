"""
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
"""

class Solution(object):
	def removeElement(self, nums, val):
		"""
		:type nums: List[int]
		:type val: int
		:rtype: int
		"""
		n = len(nums) - 1
		if n == -1:
			return 0
		while n >= 0:
			if nums[n] == val:
				del nums[n]
			n -= 1
		return len(nums)

if __name__ == "__main__":
	s = Solution()
	ex_0 = s.removeElement([1, 2, 3, 4, 4, 5], -1)
	ex_1 = s.removeElement([1, 2, 3, 4, 4, 5], 1)
	ex_2 = s.removeElement([1, 2, 3, 4, 4, 5], 4)
	ex_3 = s.removeElement([1, 2, 3, 4, 4, 5], 5)
	ex_4 = s.removeElement([1, 2, 3, 4, 4, 5], 2)
	pass