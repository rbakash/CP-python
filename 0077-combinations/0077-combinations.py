class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []

        def backtrack(currentCombination, currentNum):

            if len(currentCombination) == k:
                combinations.append(currentCombination[:])
                return

            need = k-len(currentCombination)
            remain = n-currentNum+1
            availableNumbers= remain - need

            for eachNum in range(currentNum, currentNum+availableNumbers+1 ):
                currentCombination.append(eachNum)
                backtrack(currentCombination, eachNum+1)
                currentCombination.pop()
            return

        backtrack([], 1)
        return combinations
