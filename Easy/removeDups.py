"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
"""

class Solution(object):
	def removeDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		n = len(nums)
		if not n:
			return []
		i = 1
		last = nums[0]
		while i < n:
			nums[i] = nums[i] if last != nums[i] else None
			last = last if nums[i] == None else nums[i]
			i += 1
		n -= 1
		while n > 0:
			if not nums[n]:
				del nums[n]
			n -= 1
		return nums

if __name__ == "__main__":
	s = Solution()
	n = [0,0,1,1,1,2,2,3,3,4]
	n_0 = [ 1, 1, 2 ]
	n_1 = [ 1, 2, 3, 4 ]
	n_2 = [ 1, 1, 2, 3, 4 ]
	n_3 = [ 1, 1, 2, 2, 3, 4 ]
	n_4 = [ 1, 2, 3, 4, 4 ]
	n_5 = [ 1, 2, 3, 4, 4, 5 ]

	ex = s.removeDuplicates(n)
	ex_0 = s.removeDuplicates(n_0)
	ex_1 = s.removeDuplicates(n_1)
	ex_2 = s.removeDuplicates(n_2)
	ex_3 = s.removeDuplicates(n_3)
	ex_4 = s.removeDuplicates(n_4)
	ex_5 = s.removeDuplicates(n_5)