class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        noOfIslands = 0
        if not grid:
            return noOfIslands
        rows = len(grid)
        cols = len(grid[0])

        def dfs(currentRow, currentCol):
            if (
                currentRow < 0
                or currentRow == rows
                or currentCol < 0
                or currentCol == cols
                or grid[currentRow][currentCol] != "1"
            ):
                return
            grid[currentRow][currentCol] = "0"

            dfs(currentRow - 1, currentCol)
            dfs(currentRow + 1, currentCol)
            dfs(currentRow, currentCol - 1)
            dfs(currentRow, currentCol + 1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    dfs(row, col)
                    noOfIslands += 1
        return noOfIslands
