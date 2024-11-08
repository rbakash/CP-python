class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        indices = [ i for i in range(n)]

        indices.sort(key= lambda i:(nums[i],i))
        
        minIndexSoFar =n
        maxRampWidth = 0

        for i in indices:
            maxRampWidth = max(maxRampWidth, i-minIndexSoFar)
            minIndexSoFar = min(minIndexSoFar,i)    

        return maxRampWidth