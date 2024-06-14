class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for eachAmount in range(1, amount + 1):
            for eachCoin in coins:
                if eachAmount - eachCoin >= 0:
                    dp[eachAmount] = min(dp[eachAmount], 1 + dp[eachAmount - eachCoin])

        return dp[amount] if dp[amount] != amount + 1 else -1
