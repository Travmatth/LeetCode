"""
Given a 2d grid map of '1's (land) and '0's (water),
count the number of islands. An island is surrounded
by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four
edges of the grid are all surrounded by water.
"""

class Solution(object):
    def mark_island(self, grid, y, x, rows, cols):
        grid[y][x] = '0'
        if y + 1 < rows and grid[y + 1][x] == '1':
            self.mark_island(grid, y + 1, x, rows, cols)
        if y > 0 and grid[y - 1][x] == '1':
            self.mark_island(grid, y - 1, x, rows, cols)
        if x + 1 < cols and grid[y][x + 1] == '1':
            self.mark_island(grid, y, x + 1, rows, cols)
        if x > 0 and grid[y][x - 1] == '1':
            self.mark_island(grid, y, x - 1, rows, cols)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or len(grid) == 0:
            return 0
        count, rows, cols = 0, len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    count += 1
                    self.mark_island(grid, row, col, rows, cols)
        return count

if __name__ == "__main__":
    s = Solution()
    ex_0 = s.numIslands([['1','1','1','1','0'],
        ['1','1','0','1','0'],
        ['1','1','0','0','0'],
        ['0','0','0','0','0'],])
    if ex_0 != 1:
        print("Error")
    ex_1 = s.numIslands([['1','1','0','0','0'],
        ['1','1','0','0','0'],
        ['0','0','1','0','0'],
        ['0','0','0','1','1'],])
    if ex_1 != 3:
        print("Error")
    pass