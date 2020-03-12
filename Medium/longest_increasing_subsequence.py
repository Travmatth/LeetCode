"""
Given an unsorted array of integers, find the length of longest increasing subsequence.
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:
There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n, i, longest = len(nums), 1, 1
        if n == 0:
            return 0
        dp = [1 for _ in range(n)]
        while i < n:
            j, val = 0, 0
            while j < i:
                if nums[i] > nums[j]:
                    val = max(val, dp[j])
                j += 1
            dp[i] = val + 1
            longest = max(longest, dp[i])
            i += 1
        return longest

if __name__ == "__main__":
    s = Solution()
    ex_0 = s.lengthOfLIS([10,9,2,5,3,7,101,18])
    if ex_0 != 4: 
        print("Error")
    ex_1 = s.lengthOfLIS([4,10,4,3,8,9])
    if ex_1 != 3: 
        print("Error")
    ex_2 = s.lengthOfLIS([])
    if ex_2 != 0: 
        print("Error")
    pass