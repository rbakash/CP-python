class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        first, second = 1, 2

        for index in range(3, n + 1):
            ways = first + second
            first = second
            second = ways
        return second
