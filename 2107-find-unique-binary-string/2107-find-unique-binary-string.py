class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        numSet = set(nums)
        for num in range(2**n):
            binaryString = bin(num)[2:].zfill(n)
            print(binaryString)
            if binaryString not in numSet:
                return binaryString
        return""