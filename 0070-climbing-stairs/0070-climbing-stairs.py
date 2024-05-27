class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        bestWays = [0] * (n + 1)
        bestWays[1] = 1
        bestWays[2] = 2

        for index in range(3, n + 1):
            bestWays[index] = bestWays[index - 1] + bestWays[index - 2]
        return bestWays[n]
