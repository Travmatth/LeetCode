"""
Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum and return its sum.
If you have figured out the O(n) solution, try coding another solution using
the divide and conquer approach, which is more subtle.
https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm
https://personal.utdallas.edu/~daescu/maxsa.pdf
https://www.codesdope.com/blog/article/maximum-subarray-sum-using-divide-and-conquer/
"""

class Solution(object):
    def max_sum_crossing(self, left, right):
        left_sum, right_sum = float('-inf'), float('-inf')
        left_intermediate, right_intermediate = 0, 0
        for i in reversed(left):
            left_intermediate += i
            if left_intermediate > left_sum:
                left_sum = left_intermediate
        for j in right:
            right_intermediate += j
            if right_intermediate > right_sum:
                right_sum = right_intermediate
        return left_sum + right_sum

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        mid = n // 2
        left, right  = nums[:mid], nums[mid:]
        left_sum = self.maxSubArray(left)
        right_sum = self.maxSubArray(right)
        crossing_sum = self.max_sum_crossing(left, right)
        max_sum = left_sum if left_sum > right_sum else right_sum
        max_sum = max_sum if max_sum > crossing_sum else crossing_sum
        return max_sum


if __name__ == "__main__":
    s = Solution()
    ex_0 = s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    if ex_0 != 6: #Explanation: [4,-1,2,1] has the largest sum = 6.
        print("failed")
