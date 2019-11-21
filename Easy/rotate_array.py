"""
Given an array, rotate the array to the right by k steps,
where k is non-negative.
Note:
Try to come up as many solutions as you can, there are at
least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        while k:
            last = nums.pop()
            nums.insert(0, last)
            k -= 1

if __name__ == "__main__":
    s = Solution()
    ex_0 = [1,2,3,4,5,6,7]
    s.rotate(ex_0, 3)
    if ex_0 != [5,6,7,1,2,3,4]:
        print("Error")
    ex_1 = [-1,-100,3,99]
    s.rotate(ex_1, 2)
    if ex_1 != [3,99,-1,-100]:
        print("Error")
    ex_2 = [1,2,3,4]
    s.rotate(ex_2, 5)
    if ex_2 != [4,1,2,3]:
        print("Error")
    ex_3 = [1,2,3,4,5,6,7]
    s.rotate(ex_3, 2)
    if ex_3 != [6,7,1,2,3,4,5]:
        print("Error")
    pass