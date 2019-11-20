"""
Given an array of size n, find the majority element.
The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element
always exist in the array.
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 0
        key, max = None, -1
        for k, v in freq.items():
            if v > max:
                key = k
                max = v
        return key


if __name__ == "__main__":
    s = Solution()
    ex_0 = s.majorityElement([3,2,3])
    if ex_0 != 3:
        print("error")
    ex_1 = s.majorityElement([2,2,1,1,1,2,2])
    if ex_1 != 2:
        print("error")