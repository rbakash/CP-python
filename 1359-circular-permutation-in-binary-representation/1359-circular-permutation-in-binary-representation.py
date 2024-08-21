class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        result =[]
        for i in range(1<<n):
            result.append(start ^ i^(i>>1))
        print(result)
        return result