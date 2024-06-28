class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        start, maxFrequency, currentSum = 0, 0, 0
        nums.sort()
        for end, num in enumerate(nums):
            currentSum += nums[end]
            noOfOperations = nums[end] * (end - start + 1) - currentSum
            if noOfOperations > k:
                currentSum -= nums[start]
                start += 1
                noOfOperations = nums[end] * (end - start + 1) - currentSum
            maxFrequency = max(maxFrequency, (end - start + 1))

        return maxFrequency
