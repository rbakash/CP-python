class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        contains1=False
        n = len(nums)
        # mark all zero and negative number as 1
        for index, num in enumerate(nums):
            if num == 1:
                contains1 = True
            elif num<=0 or num > n:
                nums[index] =1
        
        if not contains1:
            return 1
        
        # mark the seen num with negative at index value
        for value in range(n):
            value = abs(nums[value])
            if value == n:
                nums[0]=-abs(nums[0])
            else:
                nums[value]=-abs(nums[value])
        for i in range(1,n):
            if nums[i]>0:
                return i
        
        return n if nums[0]>0 else n+1