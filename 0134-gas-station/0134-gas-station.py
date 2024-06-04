class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total = start = 0
        for idx in range(len(gas)):
            total += gas[idx] - cost[idx]
            if total < 0:
                total = 0
                start = idx + 1
        return start
