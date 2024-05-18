class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maximumProfit = 0
        buyingPrice = 9999999999999

        for iterator in range(len(prices)):
            if prices[iterator] < buyingPrice:
                buyingPrice = prices[iterator]
            elif prices[iterator] - buyingPrice > maximumProfit:
                maximumProfit = prices[iterator] - buyingPrice

        return maximumProfit
