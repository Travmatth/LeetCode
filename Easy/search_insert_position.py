"""
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        size = len(nums)
        left = 0
        right = size - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return left

if __name__ == "__main__":
    s = Solution()
    find_1stl_even = s.searchInsert([1,3,5,7,9,11], 5)
    if find_1stl_even != 2:
        print("ERROR", "find_1stl_even")
    find_l_even = s.searchInsert([1,3,5,7,9,11], 3)
    if find_l_even != 1:
        print("ERROR", "find_1stl_even")
    find_1str_even = s.searchInsert([1,3,5,7,9,11], 7)
    if find_1str_even != 3:
        print("ERROR", "find_1str_even")
    find_r_even = s.searchInsert([1,3,5,7,9,11], 9)
    if find_r_even != 4:
        print("ERROR", "find_1stl_even")
    ins_l_even = s.searchInsert([1,3,5,7,9,11], 4)
    if ins_l_even != 2:
        print("ERROR", "find_r_even")
    ins_r_even = s.searchInsert([1,3,5,7,9,11], 10)
    if ins_r_even != 5:
        print("ERROR", "find_r_even")
    ins_beg_even = s.searchInsert([1,3,5,7,9,11], 0)
    if ins_beg_even != 0:
        print("ERROR", "find_r_even")
    ins_end_even = s.searchInsert([1,3,5,7,9,11], 13)
    if ins_end_even != 6:
        print("ERROR", "find_r_even")
    ins_middle_even = s.searchInsert([1,3,5,7,9,11], 6)
    if ins_middle_even != 3:
        print("ERROR", "find_r_even")