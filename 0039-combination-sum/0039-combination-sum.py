class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        allCombinations = []

        def dfs(index, currentCombination, total):
            if total == target:
                allCombinations.append(currentCombination[:])
                return

            if index >= len(candidates) or total > target:
                return

            currentCombination.append(candidates[index])
            dfs(index, currentCombination, total + candidates[index])
            currentCombination.pop()
            dfs(index + 1, currentCombination, total)

        dfs(0, [], 0)
        return allCombinations
