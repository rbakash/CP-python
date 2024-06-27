class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxElement = max(nums)
        currentCount = 0
        start =0
        subarrayCount =0
        
        for end,num in enumerate(nums):
            if nums[end] == maxElement:
                currentCount+=1
            while currentCount == k:
                if nums[start] == maxElement:
                    currentCount -=1
                start+=1
            subarrayCount += start

        return subarrayCount

