"""
Given two arrays, write a function to compute their intersection.
Note:
    Each element in the result should appear as many times as it shows in both
	arrays. The result can be in any order.
Follow up:
    What if the given array is already sorted? How would you optimize your
	algorithm?
    What if nums1's size is small compared to nums2's
	size? Which algorithm is better?
    What if elements of nums2 are stored on disk, and the memory is limited
	such that you cannot load all elements into the memory at once?
"""

class Solution(object):
	def intersect(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: List[int]
		"""
		dict = {}
		intersect = []
		for num in nums1:
			if num not in dict:
				dict[num] = (1, 0)
			else:
				dict[num] = (dict[num][0] + 1, 0)
		for num in nums2:
			if num not in dict:
				dict[num] = (0, 1)
			else:
				dict[num] = (dict[num][0], dict[num][1] + 1)
		for k, v in dict.items():
			appears = v[0] if v[0] < v[1] else v[1]
			for i in range(appears):
				intersect.append(k)
		return intersect

if __name__ == "__main__":
	s = Solution()
	ex_0 = s.intersect([1,2,2,1], [2,2])
	if sorted(ex_0) != [2,2]:
		print("Error")
	ex_1 = s.intersect([4,9,5], [9,4,9,8,4])
	if sorted(ex_1) != [4,9]:
		print("Error")
	pass

