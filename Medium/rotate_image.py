"""
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
Note:
You have to rotate the image in-place, which means you have to modify
the input 2D matrix directly. DO NOT allocate another 2D matrix
and do the rotation.
"""

class Solution(object):
	def rotate(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: None Do not return anything, modify matrix in-place instead.
		"""
		n = len(matrix)
		# take transpose of matrix
		for y in range(n):
			for x in range(y, n):
				matrix[y][x], matrix[x][y] = matrix[x][y], matrix[y][x]
		# reverse elements in every row of matrix
		for y in range(n):
			for x in range((n // 2)):
				rev = n - 1 - x
				matrix[y][rev], matrix[y][x] = matrix[y][x], matrix[y][rev]

if __name__ == "__main__":
	s = Solution()
	ex_0 = [[1,2,3], [4,5,6], [7,8,9]]
	s.rotate(ex_0)
	if ex_0 != [[7,4,1], [8,5,2], [9,6,3]]:
		print("Error")
	ex_1 = [[ 5, 1, 9,11], [ 2, 4, 8,10], [13, 3, 6, 7], [15,14,12,16]]
	s.rotate(ex_1)
	if ex_1 != [[15,13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7,10,11]]:
		print("Error") 
	pass
