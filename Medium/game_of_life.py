"""
According to the Wikipedia's article: "The Game of Life, also known simply as
Life, is a cellular automaton devised by the British mathematician
John Horton Conway in 1970."
Given a board with m by n cells, each cell has an initial state live (1) or
dead (0). Each cell interacts with its eight neighbors (horizontal, vertical,
diagonal) using the following four rules (taken from the above Wikipedia article):
    Any live cell with fewer than two live neighbors dies, as if caused by
	under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by
	over-population..
    Any dead cell with exactly three live neighbors becomes a live cell, as if
	by reproduction.
Write a function to compute the next state (after one update) of the board given
its current state. The next state is created by applying the above rules
simultaneously to every cell in the current state, where births and deaths occur
simultaneously.
Follow up:
    Could you solve it in-place? Remember that the board needs to be updated at
	the same time: You cannot update some cells first and then use their updated
	values to update other cells.
    In this question, we represent the board using a 2D array. In principle, the
	board is infinite, which would cause problems when the active area
	encroaches the border of the array. How would you address these problems?
"""

class Solution(object):
	def count_neighbors(self, board, y, x, rows, cols, recurse):
		count = 0
		# top left
		_y, _x = y - 1, x - 1
		if _y >= 0 and _x >= 0:
			count += board[_y][_x]
		# top
		_y, _x = y - 1, x
		if _y >= 0:
			count += board[_y][_x]
		# top right
		_y, _x = y - 1, x + 1
		if _y >= 0 and _x < cols:
			count += board[_y][_x]
		# left
		_y, _x = y, x - 1
		if _x >= 0:
			count += board[_y][_x]
		# right
		_y, _x = y, x + 1
		if _x < cols:
			count += board[_y][_x]
		# bottom left
		_y, _x = y + 1, x - 1
		if _y < rows and _x >= 0:
			count += board[_y][_x]
		# bottom
		_y, _x = y + 1, x
		if _y < rows:
			count += board[_y][_x]
		# bottom right
		_y, _x = y + 1, x + 1
		if _y < rows and _x < cols:
			count += board[_y][_x]
		return count

	def next_state(self, board, y, x, rows, cols):
		if y == rows or x == cols:
			return
		neighbors = self.count_neighbors(board, y, x, rows, cols, True)
		liveness = True if board[y][x] == 1 else False
		if liveness and neighbors < 2:
			liveness = False
		elif liveness and neighbors > 3:
			liveness = False
		elif not liveness and neighbors == 3:
			liveness = True
		next_y = y + 1 if x + 1 == cols else y
		next_x = (x + 1) % cols
		self.next_state(board, next_y, next_x, rows, cols)
		board[y][x] = 1 if liveness else 0

	def gameOfLife(self, board):
		"""
		:type board: List[List[int]]
		:rtype: None Do not return anything, modify board in-place instead.
		"""
		y, x = len(board), len(board[0])
		self.next_state(board, 0, 0, y, x)

if __name__ == "__main__":
	s = Solution()
	ex_0 = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
	s.gameOfLife(ex_0)
	if ex_0 != [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]:
		print("Error")
	pass