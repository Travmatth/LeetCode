"""
Given an array nums of n integers where n > 1,
return an array output such that output[i] is
equal to the product of all the elements of nums
except nums[i].
Follow up:
Could you solve it with constant space complexity?
(The output array does not count as extra space for
the purpose of space complexity analysis.)
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        val = 1
        lr = [1 for _ in range(len(nums))]
        rl = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            lr[i] = lr[i - 1] * nums[i - 1]
        for i in reversed(range(0, len(nums) - 1)):
            rl[i] *= rl[i + 1] * nums[i + 1]
        for i in range(len(nums)):
            lr[i] *= rl[i]
        return lr

if __name__ == "__main__":
    s = Solution()
    ex_0 = s.productExceptSelf([1,2,3,4])
    if ex_0 != [24,12,8,6]:
        print("Error")
    # Note: Please solve it without division and in O(n).
    pass