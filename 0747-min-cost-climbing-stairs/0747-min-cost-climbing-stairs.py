class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost) + 1
        minCost = [0] * n
        index = 2
        while index < n:
            minSingleStep = minCost[index - 1] + cost[index - 1]
            minSecondStep = minCost[index - 2] + cost[index - 2]
            minCost[index] = min(minSingleStep, minSecondStep)
            index += 1

        # minCost += min(cost[0],cost[1])
        return minCost[-1]
