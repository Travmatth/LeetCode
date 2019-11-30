"""
Given a collection of distinct integers, return all possible permutations.
"""

class Solution(object):
    def permutations(self, nums, out, avoid, *rest):
        if len(avoid) == len(nums):
            out.append([rest])
        else:
            for i in range(len(nums)):
                if nums[i] not in avoid:
                    avoid.add(nums[i])
                    self.permutations(nums, out, avoid, nums[i], *rest)
                    avoid.remove(nums[i])

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        out = []
        avoid = set()
        for i in range(len(nums)):
            avoid.add(nums[i])
            self.permutations(nums, out, avoid, nums[i])
            avoid.remove(nums[i])
        return out

if __name__ == "__main__":
    s = Solution()
    ex_0 = s.permute([1,2,3])
    if set(ex_0) == set([[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]):
        print("Error")