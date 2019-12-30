"""
Find the kth largest element in an unsorted array.
Note that it is the kth largest element in the
sorted order, not the kth distinct element.
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not len(nums) or not k:
            return -1
        arr = sorted(nums, reverse=True)
        return arr[k - 1]

if __name__ == "__main__":
    s = Solution()
    ex_0 = s.findKthLargest([3,2,1,5,6,4], 2)
    if ex_0 != 5:
        print("error")
    ex_1 = s.findKthLargest([3,2,3,1,2,4,5,5,6], 4)
    if ex_1 != 4:
        print("error")
    pass