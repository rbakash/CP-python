class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp={}
        def recrusive(index):
            if index in dp:
                return dp[index]
            if index >= n:
                return 1
            if s[index]=='0':
                return 0
            if index == n-1:
                return 1
            answer = recrusive(index+1)
            if index+1< n and int(s[index:index+2])<=26:
                answer += recrusive(index+2)
            dp[index]=answer
            return answer
        return recrusive(0)