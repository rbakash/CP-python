class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        maxRow = len(grid)
        maxCol = len(grid[0])
        dp=[[0] * maxCol for _ in range(maxRow)]
        print(dp)
        dp[maxRow-1][maxCol-1]=grid[maxRow-1][maxCol-1]

        for row in range(maxRow-1,-1,-1):
            for col in range(maxCol-1,-1,-1):
                if col == maxCol-1 and row != maxRow-1:
                    dp[row][col]=grid[row][col]+dp[row+1][col]
                elif row == maxRow -1 and col != maxCol-1:
                    dp[row][col]=grid[row][col]+ dp[row][col+1]
                elif row != maxRow-1 and col != maxCol-1:
                    dp[row][col]=grid[row][col]+ min(dp[row+1][col],dp[row][col+1])
                # else:
                #     dp[row][col]=grid[row][col]
        return dp[0][0]