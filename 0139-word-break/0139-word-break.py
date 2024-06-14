class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp=[False]*(n+1)  
        dp[n]=True

        for index in range(n-1,-1,-1):
            for w in wordDict:
                if (index + len(w)) <= len(s) and s[index:index+len(w)]==w:
                    dp[index] = dp[index+len(w)]
                if dp[index]:
                    break
        return dp[0]

        