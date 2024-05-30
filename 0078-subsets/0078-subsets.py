class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subsets = []

        for bitIndex in range(2**n, 2 ** (n + 1)):
            bitmask = bin(bitIndex)[3:]

            currentSubSet = []
            for index in range(n):

                if bitmask[index] == "1":
                    currentSubSet.append(nums[index])
            subsets.append(currentSubSet)
        return subsets
