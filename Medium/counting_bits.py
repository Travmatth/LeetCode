"""
Given a non negative integer number num. For every numbers i
in the range 0 ≤ i ≤ num calculate the number of 1's in their
binary representation and return them as an array.
Follow up:
It is very easy to come up with a solution with run time
O(n*sizeof(integer)). But can you do it in linear time O(n)
/possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function
like __builtin_popcount in c++ or in any other language.
"""

from typing import *

class Solution:
    def countBits(self, num: int) -> List[int]:
        counts = []
        i = 0
        while i <= num:
            count = 0
            j = i
            while j != 0:
                if j & 1:
                    count += 1 
                j >>= 1
            counts.append(count)
            i += 1
        return counts
        
if __name__ == "__main__":
    s = Solution()
    ex_0 = s.countBits(2)
    if ex_0 != [0,1,1]:
        print("error", ex_0)
    ex_1 = s.countBits(5)
    if ex_1 != [0,1,1,2,1,2]:
        print("error", ex_1)
    pass