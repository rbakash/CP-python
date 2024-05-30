class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        allPerm = []
        current = []

        def backtrack(current):
            if len(current) == len(nums):
                allPerm.append(current[:])
                return

            for num in nums:
                if num not in current:
                    current.append(num)
                    backtrack(current)
                    current.pop()

        backtrack(current)
        return allPerm
