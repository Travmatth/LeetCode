"""
Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:
    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.
"""

class Solution:
	def searchMatrix(self, matrix, target):
		"""
		:type matrix: List[List[int]]
		:type target: int
		:rtype: bool
		"""
		if not matrix:
			return False
		rows, cols = len(matrix), len(matrix[0])
		y, x = 0, cols - 1
		if not cols:
			return False
		while y < rows and x >= 0:
			if matrix[y][x] == target:
				return True
			elif matrix[y][x] > target:
				x -= 1
			else:
				y += 1
		return False

if __name__ == "__main__":
	s = Solution()
	m_0 = [[1,   4,  7, 11, 15],[2,   5,  8, 12, 19],[3,   6,  9, 16, 22],[10, 13, 14, 17, 24],[18, 21, 23, 26, 30]]
	ex_0 = s.searchMatrix(m_0, 5)
	if ex_0 != True:
		print("Error")
	ex_1 = s.searchMatrix(m_0, 20)
	if ex_1 != False:
		print("Error")
	pass