class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq={}
        minOperations=0
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1

        for num,count in freq.items():
            if count ==1:
                return -1
            minOperations += ceil(count/3)
        
        return minOperations
        