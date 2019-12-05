"""
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.
"""

class Solution(object):
    def walk(self, board, word, y, x, seen, right, bottom):
        if not word:
            return True
        first, rest = word[0], word[1:]
        seen.add((y, x))
        found = False
        # top
        if y and (y - 1, x) not in seen and board[y - 1][x] == first:
            found = self.walk(board, rest, y - 1, x, seen, right, bottom)
        # bottom
        if not found and y + 1 < bottom and (y + 1, x) not in seen and board[y + 1][x] == first:
            found = self.walk(board, rest, y + 1, x, seen, right, bottom)
        # left
        if not found and x and (y, x - 1) not in seen and board[y][x - 1] == first:
            found = self.walk(board, rest, y, x - 1, seen, right, bottom)
        # right
        if not found and x + 1 < right and (y, x + 1) not in seen and board[y][x + 1] == first:
            found = self.walk(board, rest, y, x + 1, seen, right, bottom)
        if not found:
            seen.remove((y, x))
        return found

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return False
        starts = []
        right, bottom = len(board[0]), len(board)
        for y in range(bottom):
            for x, val in enumerate(board[y]):
                if val == word[0]:
                    starts.append((y, x))
        for start in starts:
            if self.walk(board, word[1:], *start, set(), right, bottom):
                return True
        return False

if __name__ == "__main__":
    s = Solution()
    board = [['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']]
    if s.exist([], "") != False:
        print("Error")
    if s.exist([], "") != False:
        print("Error")
    if s.exist(board, "") != False:
        print("Error")
    if s.exist(board, "ABCCED") != True:
        print("Error")
    if s.exist(board, "SEE") != True:
        print("Error")
    if s.exist(board, "ABCB") != False:
        print("Error")
    if s.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS") != True:
        print("Error")
    pass