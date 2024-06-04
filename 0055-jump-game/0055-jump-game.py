class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        lastposition = len(nums)-1

        for idx in range(n-2,-1,-1):
            if idx+nums[idx]>= lastposition:
                lastposition = idx
        
        return lastposition == 0