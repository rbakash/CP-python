class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # check for all zero and goal as 0
        total = sum(nums)
        n = len(nums)
        if total == 0 and goal == 0:
            return (n * (n + 1)) // 2

        start, noOfSubArray, currentSum = 0, 0, 0
        prefixZero = 0

        for end, num in enumerate(nums):
            currentSum += num

            while start < end and (nums[start] == 0 or currentSum > goal):
                if nums[start] == 1:
                    prefixZero = 0
                else:
                    prefixZero += 1
                currentSum -= nums[start]
                start += 1

            if currentSum == goal:
                noOfSubArray += 1 + prefixZero
        return noOfSubArray
