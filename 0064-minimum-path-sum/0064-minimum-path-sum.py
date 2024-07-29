class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        maxRow = len(grid)
        maxCol = len(grid[0])
        dp = [[0] * maxCol for _ in range(maxRow)]

        dp[0][0] = grid[0][0]

        # for row in range(1,maxRow):
        #     dp[row][0] = dp[row-1][0]+grid[row][0]

        # for col in range(1,maxCol):
        #     dp[0][col] = dp[0][col-1]+grid[0][col]

        for row in range( maxRow):
            for col in range( maxCol):
                if row == 0 and col == 0:
                    continue
                elif row > 0 and col > 0:
                    dp[row][col] = grid[row][col] + min(dp[row - 1][col], dp[row][col - 1])
                elif col == 0:
                    dp[row][0] = dp[row - 1][0] + grid[row][0]
                elif row == 0:
                    dp[0][col] = dp[0][col - 1] + grid[0][col]
        return dp[maxRow - 1][maxCol - 1]
