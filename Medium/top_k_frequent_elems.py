"""
Given a non-empty array of integers,
return the k most frequent elements.
Note:
You may assume k is always valid,
1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must
be better than O(n log n), where n is
the array's size.
"""

from typing import *
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top, freq = [], defaultdict(int)
        for i in nums:
            freq[i] += 1
        for key, _ in sorted(freq.items(), key=lambda item: item[1], reverse=True):
            top.append(key)
        return top[:k]

if __name__ == "__main__":
    s = Solution()
    nums_0 = s.topKFrequent([1,1,1,2,2,3], 2)
    if nums_0 != [1,2]:
        print("error ", nums_0)
    nums_1 = s.topKFrequent([1], 1)
    if nums_1 != [1]:
        print("error ", nums_1)
    pass