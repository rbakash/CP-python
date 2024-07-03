class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
       
        n, k, noOfsubarrays = len(nums), len(pattern), 0
        result=[]
        for i in range(n - 1):
            comparision = -1
            if nums[i + 1] > nums[i]:
                comparision = 1
            elif nums[i + 1] == nums[i]:
                comparision = 0
            result.append(comparision)
        for index in range(n - k + 1):
            if result[index : index + k] == pattern:
                noOfsubarrays += 1
        return noOfsubarrays
