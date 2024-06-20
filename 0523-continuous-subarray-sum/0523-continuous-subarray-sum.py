class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixSum = 0
        remainder = {0: -1}

        for index in range(len(nums)):
            prefixSum = (prefixSum + nums[index]) % k
            if prefixSum in remainder:
                if index - remainder[prefixSum] > 1:
                    return True
            else:
                remainder[prefixSum] = index

        return False
