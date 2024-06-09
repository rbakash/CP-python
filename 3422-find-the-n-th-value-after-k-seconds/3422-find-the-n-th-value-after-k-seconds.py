class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        # prevSum =1
        # currentSum =0
        # seriesIterator =2
        # for num in range(k+1):
        #     currentSum = prevSum + (seriesIterator*(seriesIterator+1)/2)
        #     prevSum = currentSum
        #     seriesIterator+=1
        a = [1] * n
        largeMod = 10**9 + 7
        for eachK in range(k):
            for eachN in range(1, n):
                a[eachN] = (a[eachN] + a[eachN - 1]) % largeMod
        return a[-1]
