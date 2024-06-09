class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        
        a = [1] * n
        largeMod = 10**9 + 7
        for eachK in range(k):
            for eachN in range(1, n):
                a[eachN] = (a[eachN] + a[eachN - 1]) % largeMod
        return a[-1]
