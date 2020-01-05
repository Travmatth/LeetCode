"""
Given an array nums containing n + 1 integers where each integer is between 1
and n (inclusive), prove that at least one duplicate number must exist.
Assume that there is only one duplicate number, find the duplicate one.
Note:
    You must not modify the array (assume the array is read only).
    You must use only constant, O(1) extra space.
    Your runtime complexity should be less than O(n2).
    There is only one duplicate number in the array, but it could be repeated
	more than once.
"""

class Solution(object):
	def findDuplicate(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		# Find the intersection point of the two runners.
		slow = nums[0]
		fast = nums[0]
		while True:
			slow = nums[slow]
			fast = nums[nums[fast]]
			if slow == fast:
				break
		# Find the "entrance" to the cycle.
		ptr1 = nums[0]
		ptr2 = slow
		while ptr1 != ptr2:
			ptr1 = nums[ptr1]
			ptr2 = nums[ptr2]
		return ptr1

if __name__ == "__main__":
	s = Solution()
	ex_0 = s.findDuplicate([1,3,4,2,2])
	if ex_0 != 2:
		print("Error")
	ex_1 = s.findDuplicate([3,1,3,4,2])
	if ex_1 != 3:
		print("Error")
	ex_2 = s.findDuplicate([1,3,4,2,1])
	if ex_2 != 1:
		print("Error")
	ex_3 = s.findDuplicate([4,3,1,4,2])
	if ex_3 != 4:
		print("Error")
	pass