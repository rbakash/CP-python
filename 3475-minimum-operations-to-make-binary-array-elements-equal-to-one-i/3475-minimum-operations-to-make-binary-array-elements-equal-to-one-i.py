class Solution:
    def minOperations(self, nums: List[int]) -> int:
        minOperations = 0
        for index in range(len(nums) - 2):
            if nums[index] == 0:
                nums[index] = 1 - nums[index]
                nums[index + 1] = 1 - nums[index + 1]
                nums[index + 2] = 1 - nums[index + 2]
                minOperations += 1
        if nums[-1] == 0 or nums[-2] == 0:
            return -1
        print(minOperations)
        return minOperations
