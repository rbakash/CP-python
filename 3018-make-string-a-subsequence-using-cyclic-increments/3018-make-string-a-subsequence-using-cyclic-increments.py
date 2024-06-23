class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        str1Len, str2Len, j = len(str1), len(str2), 0
        for index in range(str1Len):
            if j < str2Len and (ord(str2[j]) - ord(str1[index])) % 26 <= 1:
                j += 1

        return j == str2Len
