class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        frequency = defaultdict(int)
        for num in nums:
            frequency[num] += 1
        n = len(nums)
        allPerms = []

        def backtrack(currentPerm: list) -> None:
            if len(currentPerm) == n:
                allPerms.append(currentPerm[:])
                return
            for num in frequency:
                if frequency[num] ==0:
                    continue
                
                frequency[num] -= 1
                backtrack(currentPerm[:]+[num])
                frequency[num] += 1

            return

        backtrack([])
        return allPerms
