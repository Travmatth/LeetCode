"""
Given a non-empty array of integers, every element
appears twice except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = {}
        for num in nums:
            if num in seen:
                del seen[num]
            else:
                seen[num] = 1
        for k in seen.keys():
            return k

if __name__ == "__main__":
    s = Solution()
    ex_0 = s.singleNumber([2,2,1])
    if ex_0 != 1:
        print("error")
    ex_1 = s.singleNumber([4,1,2,1,2])
    if ex_1 != 4:
        print("error")
    pass