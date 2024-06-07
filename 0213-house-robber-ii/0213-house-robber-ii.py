class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if not n:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        def maxRobFrom(houseMoney: List[int]) -> int:

            prevMax, secondMax = max(houseMoney[0], houseMoney[1]), houseMoney[0]

            for index in range(2, len(houseMoney)):
                prevMax, secondMax = (
                    max(prevMax, secondMax + houseMoney[index]),
                    prevMax,
                )
            return prevMax

        return max(maxRobFrom(nums[:-1]), maxRobFrom(nums[1:]))
