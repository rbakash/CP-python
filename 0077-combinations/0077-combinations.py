class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        visited = set()

        def backtrack(currentCombination, currentN):

            if len(currentCombination) == k:
                combinations.append(currentCombination[:])
                return
            for eachNum in range(currentN, n+1 ):
                currentCombination.append(eachNum)
                backtrack(currentCombination, eachNum+1)
                currentCombination.pop()
            return

        backtrack([], 1)
        return combinations
