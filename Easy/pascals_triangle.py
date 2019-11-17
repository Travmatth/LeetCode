"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal = []
        for i in range(numRows):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    val = 1
                else:
                    val = pascal[i - 1][j] + pascal[i - 1][j - 1]
                row.append(val)
            pascal.append(row)
        return pascal

if __name__ == "__main__":
    s = Solution()
    ex_0 = s.generate(5)
    if ex_0 != [ [1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1] ]:
        print("ERROR")
    pass
