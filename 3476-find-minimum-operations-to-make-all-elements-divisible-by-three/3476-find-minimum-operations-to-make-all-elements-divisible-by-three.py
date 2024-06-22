class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        minOperations = 0
        for eachNum in nums:
            if eachNum % 3 ==0:
                minOperations +=1
        print(minOperations)
        return len(nums) - minOperations
        