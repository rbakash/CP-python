class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniqueList = set(nums)
        if len(uniqueList) == len(nums):
            return False
        else:
            return True