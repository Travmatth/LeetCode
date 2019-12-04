"""
Given a collection of intervals, merge all overlapping intervals.
"""

class Solution(object):
    def sort_key(self, lst):
        return lst[0]

    def merge(self, intervals):
        i, out, n = 0, [], len(intervals)
        intervals.sort(key=self.sort_key)
        while i < n:
            j = 1
            first = intervals[i]
            merged = [first[0], first[1]]
            while i + j < n:
                second = intervals[i + j]
                if merged[1] < second[0]:
                    break
                elif merged[1] < second[1]:
                    merged[1] = second[1]
                j += 1
            out.append(merged)
            i += j
        return out

if __name__ == "__main__":
    s = Solution()
    ex_0 = s.merge([[1, 3], [2, 6], [8, 10], [15, 18]])
    if ex_0 != [[1, 6], [8, 10], [15, 18]]:
        print("Error")
    ex_1 = s.merge([[1, 4], [4, 5]])
    if ex_1 != [[1, 5]]:
        print("Error")
    ex_2 = s.merge([[20, 25], [1, 5], [10, 15], [4, 11]])
    if ex_2 != [[1, 15], [20, 25]]:
        print("Error")
    ex_3 = s.merge([[1, 4], [2, 3]])
    if ex_3 != [[1, 4]]:
        print("Error")
    pass