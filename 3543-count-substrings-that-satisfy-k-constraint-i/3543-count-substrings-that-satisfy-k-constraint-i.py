class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        length=0
        for i in range(len(s)):
            oneCount,zeroCount =0,0
            for j in range(i,len(s)):
                if s[j]=="1":
                    oneCount+=1
                else:
                    zeroCount+=1
                if oneCount<=k or zeroCount<=k:
                    length+=1
        return length