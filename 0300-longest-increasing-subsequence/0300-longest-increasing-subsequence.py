class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]* len(nums)
        maxLength= 1
        for index in range(1,len(nums)):
            for j in range(index):
                if nums[index]>nums[j]:
                    dp[index] = max(dp[index],dp[j]+1)
                    if dp[index]> maxLength:
                        maxLength = dp[index]
        
        return maxLength