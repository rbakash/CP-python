class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        pairs = [(eachSpeed,eachEfficinecy) for eachSpeed,eachEfficinecy in zip(speed, efficiency)]
        pairs.sort(key=lambda x: x[1], reverse=True)
        print(pairs)
        minHeap = []
        maxSum = 0
        currentSpeedSum = 0
        for eachSpeed,eachEfficinecy in pairs:
            currentSpeedSum += eachSpeed
            heappush(minHeap, eachSpeed)

            if len(minHeap) > k:
                currentSpeedSum -= heappop(minHeap)
            maxSum = max(maxSum, currentSpeedSum * eachEfficinecy)
        
        return maxSum % (10**9+7)