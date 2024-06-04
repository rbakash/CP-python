class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        start,end =0,0
        # we know length of num is atleast 1
        currentSum=nums[0]
        maxSum=nums[0]

        for index in range(1,len(nums)):
            currentSum = max(nums[index],currentSum+nums[index])

            # if we reset the currentSum
            if currentSum == nums[index]:
                start=index
                end=index
            if currentSum > maxSum:
                maxSum = currentSum
                end = index
            
        return maxSum
        