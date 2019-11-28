"""
Given an array nums of n integers, are there elements a, b, c in nums
such that a + b + c = 0? Find all unique triplets in the array which
gives the sum of zero.
Note:
The solution set must not contain duplicate triplets.
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solutions, n = set(), len(nums)
        nums.sort()
        for first_i in range(n - 2):
            second_i = first_i + 1
            third_i = n - 1
            while second_i < third_i:
                summation = nums[first_i] + nums[second_i] + nums[third_i]
                if summation == 0:
                    solutions.add((nums[first_i], nums[second_i], nums[third_i]))
                    second_i += 1
                    third_i -= 1
                elif summation < 0:
                    second_i += 1
                else:
                    third_i -= 1
        return [[i for i in triplet] for triplet in solutions]

if __name__ == "__main__":
    s = Solution()
    ex_0 = s.threeSum([-1, 0, 1, 2, -1, -4])
    if ex_0 != [[-1, 0, 1], [-1, -1, 2]]:
        print("Error")
    ex_1 = s.threeSum([])
    if ex_1 != []:
        print("Error")
    ex_1 = s.threeSum([0, 0, 0])
    if ex_1 != []:
        print("Error")
    ex_2 = s.threeSum([-2, 0, 1, 1, 2])
    if ex_2 != []:
        print("Error")
    pass