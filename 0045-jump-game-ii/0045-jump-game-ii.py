class Solution:
    def jump(self, nums: List[int]) -> int:
        noOfJumps = 0
        left = right = 0
        n = len(nums) - 1

        while right < n:
            maxJump = 0
            for idx in range(left, right + 1):
                maxJump = max(maxJump, idx + nums[idx])
            left = right + 1
            right = maxJump
            noOfJumps += 1

        return noOfJumps
