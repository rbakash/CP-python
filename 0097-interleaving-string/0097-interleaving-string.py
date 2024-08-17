class Solution:
    def isInterleaveEditorial(self, s1: str, s2: str, s3: str) -> bool:
        def recursive(s1,i,s2,j,s3,k):
            if i ==len(s1):
                return s2[j:]==s3[k:]
            if j==len(s2):
                return s1[i:] == s3[k:]
            if self.dp[i][j] != -1:
                return self.dp[i][j] ==1
            ans = False
            if (s1[i]==s3[k] and recursive(s1,i+1,s2,j,s3,k+1)) or (s2[j]==s3[k] and recursive(s1,i,s2,j+1,s3,k+1)):
                ans = True
            self.dp[i][j] = 1 if ans else 0
            return ans
        if len(s1)+len(s2) != len(s3):
            return False
        self.dp=[[-1]* len(s2) for _ in range(len(s1))]
        return recursive(s1,0,s2,0,s3,0)


    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp={}
        def recursive(i,j,k):
            if k == len(s3):
                return i == len(s1) and j == len(s2)
            if (i,j) in dp:
                return dp[(i,j)]
            ans = False
            if i < len(s1) and s1[i] ==s3[k]:
                if recursive(i+1,j,k+1):
                    dp[(i,j)]= True
                    return True
            if j < len(s2) and s2[j] ==s3[k]:
                if recursive(i,j+1,k+1):
                    dp[(i,j)]= True
                    return True
            dp[(i,j)]=False
            return False
        return recursive(0,0,0)
            


