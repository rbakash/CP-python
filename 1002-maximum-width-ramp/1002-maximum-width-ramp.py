class Solution:
    def maxWidthRampSorting(self, nums: List[int]) -> int:
        n = len(nums)
        indices = [ i for i in range(n)]

        indices.sort(key= lambda i:(nums[i],i))
        
        minIndexSoFar =n
        maxRampWidth = 0

        for i in indices:
            maxRampWidth = max(maxRampWidth, i-minIndexSoFar)
            minIndexSoFar = min(minIndexSoFar,i)    

        return maxRampWidth
    # Monotonic Stack solution
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack =[]
        n = len(nums)
        for index in range(n):
            if not stack or nums[index] < nums[stack[-1]]:
                stack.append(index)
        maxWidth = 0
        for index in range(n-1,-1,-1):
            while stack and nums[stack[-1]]<=nums[index]:
                maxWidth = max(maxWidth, (index - stack[-1]))
                stack.pop()
        return maxWidth