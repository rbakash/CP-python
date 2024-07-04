class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        while len(nums) > 1:
            newArray=[]
            for index in range(len(nums)-1):
                newArray.append((nums[index] + nums[index + 1])%10)
            nums=newArray[:]
        return nums[0]
