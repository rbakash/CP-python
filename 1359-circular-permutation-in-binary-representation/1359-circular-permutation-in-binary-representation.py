class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        result =[]
        for i in range(2**n):
            result.append(i^(i>>1))
        startIndex = result.index(start)
        result = result[startIndex:]+result[:startIndex]
        return result