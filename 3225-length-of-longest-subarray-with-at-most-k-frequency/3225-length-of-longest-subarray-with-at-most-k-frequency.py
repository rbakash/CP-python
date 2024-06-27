class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        start =0
        maxLength = 0
        frequency=defaultdict(int)

        for end,num in enumerate(nums):
            frequency[num]+=1
            
            while frequency[num] >k and start <= end:
                frequency[nums[start]]-=1
                start+=1
                
            maxLength = max(maxLength, (end-start+1))

        return maxLength 