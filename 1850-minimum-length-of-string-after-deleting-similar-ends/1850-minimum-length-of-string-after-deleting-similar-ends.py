class Solution:
    def minimumLength(self, s: str) -> int:
        start,end = 0, len(s)-1

        while start < end and s[start] == s[end]:
            currentCharacter = s[start]

            while start<=end and s[start] == currentCharacter:
                start+=1
            
            while start<end and s[end] == currentCharacter:
                end-=1
        
        return end-start+1