class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixSum =[0]*(k)
        prefixSum[0]=1
        noOfSubArrays,prefixIndex =0,0

        # prefix & suffix sum
        for num in nums:
            prefixIndex = (prefixIndex+(num %k)+k)%k
            noOfSubArrays += prefixSum[prefixIndex]
            prefixSum[prefixIndex] = prefixSum[prefixIndex]+1
            
        return noOfSubArrays


