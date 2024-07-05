class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def findTheSum(divisor: int) -> int:
            currentSum = 0
            for num in nums:
                currentSum += math.ceil(num / divisor)
            return currentSum

        low, high = 1, max(nums)
        minThreshold, minSum = 1, 1
        while low <= high:
            mid = low + (high - low) // 2
            minThreshold = findTheSum(mid)
            if minThreshold <= threshold:
                high = mid - 1
            else:
                low = mid + 1
        return low
