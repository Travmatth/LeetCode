"""
You are a professional robber planning to rob houses
along a street. Each house has a certain amount of money
stashed, the only constraint stopping you from robbing each
of them is that adjacent houses have security system connected
and it will automatically contact the police if two adjacent
houses were broken into on the same night.
Given a list of non-negative integers representing the amount of
money of each house, determine the maximum amount of money you
can rob tonight without alerting the police.
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current, prev = 0, 0

        for num in nums:
            next = current if current > prev + num else prev + num
            prev = current
            current = next
        return current

if __name__ == "__main__":
    s = Solution()
    # Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
    # Total amount you can rob = 1 + 3 = 4.
    ex_0 = s.rob([1,2,3,1])
    if ex_0 != 4:
        print("Error")
    # Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
    # Total amount you can rob = 2 + 9 + 1 = 12.
    ex_2 = s.rob([2,7,9,3,1])
    if ex_2 != 12:
        print("Error")
    pass