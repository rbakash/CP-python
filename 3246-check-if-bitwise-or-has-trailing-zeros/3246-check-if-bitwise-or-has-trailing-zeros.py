class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        evenCount = 0
        for num in nums:
            if num % 2 == 0:
                evenCount += 1
            if evenCount >= 2:
                return True
        return False
