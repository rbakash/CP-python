class Solution:
    def minOperations(self, nums: List[int]) -> int:
        minOperations = 0
        for num in nums:
            if num ==0:
                # If you have flipped even times, then this is final state of the num
                # Need to flip this
                if minOperations %2 ==0:
                    minOperations+=1
            else:
                # The 1 might be flipped before, so we need to check the flipped state
                # the 1 will be 0 if we have flipped odd times before
                if minOperations % 2 ==1:
                    minOperations +=1
        return minOperations
