"""
Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
"""

class Solution(object):
	def gen_sets(self, nums, i, n, cur, power_set):
		if i == n:
			return power_set
		power_set.append([x for x in cur])
		for j in range(i + 1, n):
			cur.append(nums[j])
			self.gen_sets(nums, j, n, cur, power_set)
			cur.pop()
		return power_set

	def subsets(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		return self.gen_sets(nums, -1, len(nums), [], [])

if __name__ == "__main__":
	s = Solution()    
	ex_0 = s.subsets([1,2,3])
	if ex_0 != [[3], [1], [2], [1,2,3], [1,3], [2,3], [1,2], []]:
		print("Error")
	pass