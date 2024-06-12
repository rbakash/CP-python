class Solution:
    def countSubstrings(self, s: str) -> int:
        palindromicStrings=[]
        count =0
        n = len(s)

        for index in range(n):
            left = right =index
            while left>=0 and right<n and s[left]==s[right]:
                palindromicStrings.append(s[left:right+1])
                count+=1
                left-=1
                right+=1
        
            left =index
            right = left+1

            while left>=0 and right<n and s[left]==s[right]:
                palindromicStrings.append(s[left:right+1])
                count+=1
                left-=1
                right+=1

        return count
        