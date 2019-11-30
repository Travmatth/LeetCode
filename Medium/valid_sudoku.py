"""
Determine if a 9x9 Sudoku board is valid. Only the filled
cells need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9
without repetition.
A partially filled sudoku which is valid.
The Sudoku board could be partially filled, where empty cells
are filled with the character '.'.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.
"""

import math

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if not board:
            return False
        centers = [(1, 1), (4, 1), (7, 1), (1, 4), (4, 4), (7, 4), (1, 7), (4, 7), (7, 7)]
        # index of nums == number on board
        nums = [[] for i in range(10)]
        # iter through board and store x,y of every cell
        for y, row in enumerate(board):
            for x, val in enumerate(row):
                if val != ".":
                    num = ord(val) - ord("0")
                    nums[num].append((x, y))
        # filter out numbers with less than one, as they cannot repeat
        nums = [(v if len(v) > 1 else None) for v in nums]
        # iter all numbers
        for i in range(10):
            # iter all pairs in number
            if nums[i]:
                # compare all pairs against each other
                pairs = nums[i]
                for j in range(len(pairs)):
                    for k in range(j + 1, len(pairs)):
                        first = pairs[j]
                        second = pairs[k]
                        # verify not same col:
                        if first[0] == second[0]:
                            return False
                        # verify not same row
                        elif first[1] == second[1]:
                            return False
                        # verify not same subsquare - compare euclidian dist from center of subsquare
                        for center in centers:
                            p, q = first[0] - center[0], first[1] - center[1]
                            dist_1 = math.sqrt((p**2) + (q**2)) // 1
                            if dist_1 == 1 or first == center:
                                p, q = second[0] - center[0], second[1] - center[1]
                                dist_2 = math.sqrt((p**2) + (q**2)) // 1
                                if dist_2 == 1 or second == center:
                                    return False
        return True

if __name__ == "__main__":
    s = Solution()
    ex_0 = s.isValidSudoku([
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ])
    if ex_0 != True:
        print("Error")
    ex_1 = s.isValidSudoku([
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ])
    if ex_1 != False:
        print("Error")
    #first == (7, 0) and second == (8, 2)
    ex_2 = s.isValidSudoku([
        [".",".",".", ".","5",".", ".","1","."],
        [".","4",".", "3",".",".", ".",".","."],
        [".",".",".", ".",".","3", ".",".","1"],

        ["8",".",".", ".",".",".", ".","2","."],
        [".",".","2", ".","7",".", ".",".","."],
        [".","1","5", ".",".",".", ".",".","."],

        [".",".",".", ".",".","2", ".",".","."],
        [".","2",".", "9",".",".", ".",".","."],
        [".",".","4", ".",".",".", ".",".","."]
    ])
    if ex_2 != False:
        print("Error")
    ex_3 = s.isValidSudoku([
        ["9",".",".", "6",".",".", ".",".","."],
        [".",".",".", ".","6",".", ".",".","."],
        [".",".",".", ".",".","1", ".","3","."],

        [".",".",".", ".",".",".", ".",".","8"],
        [".",".",".", ".",".","8", ".",".","."],
        [".",".",".", "4",".",".", "2",".","."],

        [".",".",".", ".",".",".", ".",".","1"],
        ["6",".",".", ".","1",".", ".",".","."],
        [".",".",".", ".",".",".", ".",".","."]
    ])
    if ex_3 != False:
        print("Error")
    pass