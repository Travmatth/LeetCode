"""
Given a list of non negative integers, arrange them such that
they form the largest number.
Note: The result may be very large, so you need to return a
string instead of an integer.
"""

class Solution(object):
    def compare(self, l, r):
        return True if l + r > r + l else False

    def sort(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        n = len(nums)
        if n == 1:
            return [str(nums[0])]
        mid = n // 2
        out = []
        l, r = self.sort(nums[:mid]), self.sort(nums[mid:])
        l_n, r_n, i, j = len(l), len(r), 0, 0
        while i < l_n and j < r_n:
            if self.compare(l[i], r[j]):
                out.append(l[i])
                i += 1
            else:
                out.append(r[j])
                j += 1
        if j < r_n:
            out += r[j:]
        elif i < l_n:
            out += l[i:]
        return out
    
    def largestNumber(self, nums):
        ret = "".join(self.sort(nums))
        if ret[0] == "0":
            return "0"
        return ret
        

if __name__ == "__main__":
    s = Solution()
    ex_0 = s.largestNumber([10,2])
    if ex_0 != "210":
        print("Error")
    ex_1 = s.largestNumber([3,30,34,5,9])
    if ex_1 != "9534330":
        print("Error")
    ex_2 = s.largestNumber([0,0])
    if ex_2 != "0":
        print("Error")
    pass