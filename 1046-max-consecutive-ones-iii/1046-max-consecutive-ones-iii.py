class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        noOfZeros,maxLength,start =0, 0,0

        for end,num in enumerate(nums):
            if num == 0:
                noOfZeros +=1
            
            # Shrink the window to just have k number of zeros
            while noOfZeros > k:
                if nums[start]==0:
                    noOfZeros-=1
                start+=1

            # max consecutive length
            maxLength = max(maxLength, (end-start+1))
        
        return maxLength
