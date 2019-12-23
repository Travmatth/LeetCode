"""
A peak element is an element that is greater than its neighbors.
Given an input array nums, where nums[i] ≠ nums[i+1], find a peak
element and return its index.
The array may contain multiple peaks, in that case return the index
to any one of the peaks is fine.
You may imagine that nums[-1] = nums[n] = -∞.
"""

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0
        elif n == 2:
            return 0 if nums[0] > nums[1] else 1
        elif n == 3:
            if nums[1] > nums[0] and nums[1] > nums[2]:
                return 1
        mid = n // 2
        l, r = self.findPeakElement(nums[:mid]), mid + self.findPeakElement(nums[mid:])
        return l if nums[l] > nums[r] else r

if __name__ == "__main__":
    s = Solution()
    ex_0 = s.findPeakElement([1,2,3,1])
    if ex_0 != 2:
        print("Error")
    # Explanation: 3 is a peak element and your function should return the index number 2.
    ex_1 = s.findPeakElement([1,2,1,3,5,6,4])
    if ex_1 != 1 and ex_1 != 5: 
        print("Error")
    # Explanation: Your function can return either index number 1 where the peak element is 2, 
    # or index number 5 where the peak element is 6.
    pass