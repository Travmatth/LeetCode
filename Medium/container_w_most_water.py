"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two
lines, which together with x-axis forms a container, such that the container contains the most water.
Note: You may not slant the container and n is at least 2.
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max, l, r = -(1 << 31), 0, len(height) - 1
        while l < r:
            min = height[l] if height[l] < height[r] else height[r]
            _max = (r - l) * min
            max = _max if _max > max else max
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max

if __name__ == "__main__":
    s = Solution()
    ex_0 = s.maxArea([1,8,6,2,5,4,8,3,7])
    if ex_0 != 49:
        print("Error")
    pass