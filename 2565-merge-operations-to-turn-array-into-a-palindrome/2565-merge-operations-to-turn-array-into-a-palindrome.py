class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        numberOfOperations = 0

        while left < right:

            if nums[left] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] < nums[right]:
                nums[left + 1] += nums[left]
                nums[left] *= -1
                left += 1
                numberOfOperations += 1
            else:
                nums[right - 1] += nums[right]
                nums[right] *= -1
                right -= 1
                numberOfOperations += 1
        nums = [num for num in nums if num >= 0]
        return numberOfOperations
