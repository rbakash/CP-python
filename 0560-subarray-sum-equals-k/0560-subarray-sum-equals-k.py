class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currentSum=0
        prefixSum={0:1}
        numberOfSubArray =0
        for idx, num in enumerate(nums):
            currentSum += num
            if currentSum - k in prefixSum:
                numberOfSubArray+=prefixSum[currentSum - k]
            if currentSum in prefixSum:
                prefixSum[currentSum]+=1
            else:
                prefixSum[currentSum]=1
        return numberOfSubArray
        