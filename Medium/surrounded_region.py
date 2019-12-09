"""
Given a 2D board containing 'X' and 'O' (the letter O),
capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in
that surrounded region.
Surrounded regions shouldn’t be on the border, which means
that any 'O' on the border of the board are not flipped to
'X'. Any 'O' that is not on the border and it is not
connected to an 'O' on the border will be flipped to 'X'.
Two cells are connected if they are adjacent cells connected
horizontally or vertically.
"""

class Solution(object):
    def mark(self, board, y, x, cols, rows):
        if y == -1 or x == -1:
            return
        elif y == rows or x == cols:
            return
        elif board[y][x] == 'X' or board[y][x] == '-':
            return
        board[y][x] = '-'
        self.mark(board, y - 1, x, cols, rows)
        self.mark(board, y + 1, x, cols, rows)
        self.mark(board, y, x - 1, cols, rows)
        self.mark(board, y, x + 1, cols, rows)

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        if not rows:
            return
        cols = len(board[0])
        # mark top, bottom
        for x in range(cols):
            if board[0][x] == 'O':
                self.mark(board, 0, x, cols, rows)
            if board[rows - 1][x] == 'O':
                self.mark(board, rows - 1, x, cols, rows)
        # mark left, right
        for y in range(rows):
            if board[y][0] == 'O':
                self.mark(board, y, 0, cols, rows)
            if board[y][cols - 1] == 'O':
                self.mark(board, y, cols - 1, cols, rows)
        # all regions surrounding border marked '-', all '0' should change
        for y in range(rows):
            for x in range(cols):
                if board[y][x] == '-':
                    board[y][x] = 'O'
                elif board[y][x] == 'O':
                    board[y][x] = 'X'

if __name__ == "__main__":
    s = Solution()
    m_0 = [['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'O', 'X', 'X']]
    s.solve(m_0)
    if m_0 != [['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'O', 'X', 'X']]:
        print("Error")
    m_1 = []
    s.solve(m_1)
    if m_1 != []:
        print("Error")
    m_2 = [["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]
    s.solve(m_2)
    if m_2 != [["O","X","X","O","X"],["X","X","X","X","O"],["X","X","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]:
        print("Error")
    m_3 = [["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]]
    s.solve(m_3)
    if m_3 != [["O","X","X","O","X"],["X","X","X","X","O"],["X","X","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]:
        print("Error")

    pass