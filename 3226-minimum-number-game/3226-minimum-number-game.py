class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        index = 0
        while index < len(nums):
            nums[index],nums[index+1]= nums[index+1],nums[index]
            index+=2
        return nums