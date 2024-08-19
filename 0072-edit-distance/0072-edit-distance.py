class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp=[[-1]*(len(word2)+1) for _ in range(len(word1)+1)]
        def recur(word1Index,word2Index):
            if word1Index == 0:
                return word2Index
            if word2Index == 0:
                return word1Index
            if dp[word1Index][word2Index] != -1:
                return dp[word1Index][word2Index]
            if word1[word1Index-1] == word2[word2Index-1]:
                dp[word1Index][word2Index] = recur(word1Index-1,word2Index-1)
            else:
                insertOperations = recur(word1Index,word2Index-1)
                deleteOperations = recur(word1Index-1,word2Index)
                replaceOperations = recur(word1Index-1,word2Index-1)
                dp[word1Index][word2Index] =  1 + min(insertOperations,deleteOperations,replaceOperations)
            return dp[word1Index][word2Index]
        return recur(len(word1),len(word2))