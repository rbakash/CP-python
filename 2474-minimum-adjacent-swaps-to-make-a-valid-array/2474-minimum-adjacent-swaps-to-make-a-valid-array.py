class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:

        iterator = 0
        noOfSwaps = 0
        n = len(nums)-1
        maxValue = float("-inf")
        maxIndex = -1
        minValue = float("inf")
        minIndex = -1

        for index, num in enumerate(nums):
            if num < minValue:
                minIndex = index
                minValue = num
            if num >= maxValue:
                maxIndex = index
                maxValue = num

        noOfSwaps = (minIndex - 0) + (n - maxIndex)
        if minIndex > maxIndex:
            noOfSwaps -= 1
        return noOfSwaps
        # iterator = minIndex
        # # calculate the swaps needed for highest number
        # while iterator < n - 1:
        #     if nums[iterator] > nums[iterator + 1]:
        #         nums[iterator + 1], nums[iterator] = nums[iterator], nums[iterator + 1]
        #         noOfSwaps += 1
        #     iterator += 1

        # # calculate the swaps needed for lowest number
        # iterator = n - 1

        # while iterator > 0:
        #     if nums[iterator] < nums[iterator - 1]:
        #         nums[iterator - 1], nums[iterator] = nums[iterator], nums[iterator - 1]
        #         noOfSwaps += 1
        #     iterator -= 1

        # return noOfSwaps
