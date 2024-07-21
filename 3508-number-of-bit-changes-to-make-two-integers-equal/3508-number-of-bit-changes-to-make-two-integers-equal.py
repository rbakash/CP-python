class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if n == k:
            return 0

        binN = bin(n)[2:]
        binK = bin(k)[2:]
        maxLen = max(len(binN),len(binK))
        binN = list(binN.zfill(maxLen))
        binK = list(binK.zfill(maxLen))
        count = 0

        for index in range(len(binN)):
            
            if binN[index] == '0':
                if binN[index] != binK[index]:
                    return -1
            elif binN[index] !=binK[index]:
                binN[index] = '0'
                count += 1
            # print(binN,binK,count)
            if binN == binK:
                return count
        return -1
