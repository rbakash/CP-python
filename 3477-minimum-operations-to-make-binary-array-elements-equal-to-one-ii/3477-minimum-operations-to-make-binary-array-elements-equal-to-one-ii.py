class Solution:
    def minOperations(self, nums: List[int]) -> int:
        minOperations = 0
        for num in nums:
            if num ==0:
                if minOperations %2 ==0:
                    minOperations+=1
            else:
                if minOperations % 2 ==1:
                    minOperations +=1
        return minOperations
