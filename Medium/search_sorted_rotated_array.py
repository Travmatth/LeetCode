"""
Suppose an array sorted in ascending order is rotated
at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in
the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the
order of O(log n).
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        low, high = 0, len(nums) - 1
        return self.bin_search(nums, target, low, high)

    def bin_search(self, nums, target, low, high):
        mid = (low + high) // 2
        if low > high:
            return -1
        elif nums[mid] == target:
            return mid
        # if left half is sorted
        elif nums[low] <= nums[mid]:
            # if key is in left half:
            if target >= nums[low] and target <= nums[mid]:
                return self.bin_search(nums, target, low, mid)
            # else target is in right half
            return self.bin_search(nums, target, mid + 1, high)
        # if right half is sorted
        else:
            # if target is in right half:
            if target >= nums[mid] and target <= nums[high]:
                return self.bin_search(nums, target, mid + 1, high)
            # else target is in left half
            return self.bin_search(nums, target, low, mid)

if __name__ == "__main__":
    s = Solution()
    ex_0 = s.search([4, 5, 6, 7, 0, 1, 2], 0)
    if ex_0 != 4:
        print("Error")
    ex_1 = s.search([4, 5, 6, 7, 0, 1, 2], 3)
    if ex_1 != -1:
        print("Error")
    ex_2 = s.search([0, 1, 2, 4, 5, 6, 7, 8, 9], 3)
    if ex_2 != -1:
        print("Error")
    ex_3 = s.search([5, 1, 3], 5)
    if ex_3 != 0:
        print("Error")
    pass
