"""
Given an array of non-negative integers, you are
initially positioned at the first index of the array.
Each element in the array represents your maximum
jump length at that position.
Determine if you are able to reach the last index.
"""

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n <= 1:
            return True
        last = n - 1
        for i in reversed(range(n)):
            if i + nums[i] >= last:
                last = i
        return last == 0

if __name__ == "__main__":
    s = Solution()
    ex_0 = s.canJump([2, 3, 1, 1, 4])
    if ex_0 != True:
        print("Error")
    # Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
    ex_1 = s.canJump([3, 2, 1, 0, 4])
    if ex_1 != False:
        print("Error")
    # Explanation: You will always arrive at index 3 no matter what. Its maximum
    # jump length is 0, which makes it impossible to reach the last index.
    ex_2 = s.canJump([2, 5, 0, 0])
    if ex_2 != True:
        print("Error")
    ex_3 = s.canJump([2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6])
    if ex_3 != True:
        print("Error")
    pass