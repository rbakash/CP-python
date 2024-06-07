class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        maxRobbery = [nums[0],max(nums[0],nums[1])]

        for index in range(2, n):
            maxRobbery.append(max(
                maxRobbery[index - 1], maxRobbery[index - 2] + nums[index]
            ))
        print(maxRobbery)
        return maxRobbery[n-1]
