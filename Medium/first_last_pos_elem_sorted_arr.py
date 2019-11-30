"""
Given an array of integers nums sorted in ascending order,
find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].
"""

class Solution(object):
    def bin_search(self, nums, target, low, high, start):
        mid = (low + high) // 2
        if low > high:
            return -1
        elif nums[mid] != target:
            if nums[mid] < target:
                return self.bin_search(nums, target, mid + 1, high, start)
            return self.bin_search(nums, target, low, mid - 1, start)
        elif start and (not mid or nums[mid - 1] != target):
            return mid
        elif start:
            return self.bin_search(nums, target, low, mid - 1, start)
        elif not start and (len(nums) == mid + 1 or nums[mid + 1] != target):
            return mid
        elif not start:
            return self.bin_search(nums, target, mid + 1, high, start)

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        return [self.bin_search(nums, target, 0, len(nums) - 1, True), self.bin_search(nums, target, 0, len(nums) - 1, False)]

if __name__ == "__main__":
    s = Solution()
    ex_0 = s.searchRange([5, 7, 7, 8, 8, 10], 8)
    if ex_0 != [3, 4]:
        print("Error")
    ex_1 = s.searchRange([5, 7, 7, 8, 8, 10], 6)
    if ex_1 != [-1, -1]:
        print("Error")
    ex_2 = s.searchRange([5, 7, 7, 8, 8, 10], 5)
    if ex_2 != [0, 0]:
        print("Error")
    ex_3 = s.searchRange([2, 2], 2)
    if ex_3 != [0, 1]:
        print("Error")
    pass