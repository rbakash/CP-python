class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixForRemainder =[0]*(k)
        prefixForRemainder[0]=1
        noOfSubArrays,prefixIndex =0,0

        # prefix & suffix sum
        for num in nums:
            prefixIndex = (prefixIndex+(num %k)+k)%k
            noOfSubArrays += prefixForRemainder[prefixIndex]
            prefixForRemainder[prefixIndex] = prefixForRemainder[prefixIndex]+1
            
        return noOfSubArrays


