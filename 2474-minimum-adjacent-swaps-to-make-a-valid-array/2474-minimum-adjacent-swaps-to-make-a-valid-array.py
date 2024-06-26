class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:

        noOfSwaps = 0
        n = len(nums)

        if n == 1:
            return 0

        maxIndex = 0
        minIndex = 0
        print(nums[::-1])
        for index in range(1, n):
            if nums[index] < nums[minIndex]:
                minIndex = index
                # minValue = nums[index]
            if nums[index] >= nums[maxIndex]:
                maxIndex = index
                # maxValue = nums[index]

        noOfSwaps = (minIndex) + (n - 1 - maxIndex)
        if minIndex > maxIndex:
            noOfSwaps -= 1
        return noOfSwaps
