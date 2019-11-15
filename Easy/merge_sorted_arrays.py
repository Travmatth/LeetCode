"""
Given two sorted integer arrays nums1 and nums2,
merge nums2 into nums1 as one sorted array.
Note:
    The number of elements initialized in nums1 and nums2
        are m and n respectively.
    You may assume that nums1 has enough space (size that
        is greater or equal to m + n) to hold additional
        elements from nums2.
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for i in reversed(range(m, len(nums1))):
            del nums1[i]
        i = 0
        for j in nums2:
            while i < len(nums1) and nums1[i] < j:
                i += 1
            nums1.insert(i, j)

if __name__ == "__main__":
    s = Solution()
    n_0 = [1,2,3,0,0,0]
    n_1 = [2,5,6]
    s.merge(n_0, 3, n_1, 3)
    pass