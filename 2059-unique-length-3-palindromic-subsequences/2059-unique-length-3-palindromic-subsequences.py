class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        firstOccurence,lastOccurence=[-1]*26,[-1]*26
        for index in range(len(s)):
            charIndex = ord(s[index])-ord('a')
            if firstOccurence[charIndex]==-1:
                firstOccurence[charIndex]=index
            lastOccurence[charIndex]=index
        noOfPalindromes =0
        
        for index in range(26):
            if firstOccurence[index]==-1:
                continue
            uniqueCharacters=set(s[firstOccurence[index]+1:lastOccurence[index]])
            # for k in range(firstOccurence[index]+1,lastOccurence[index]):
            #     uniqueCharacters.add(s[k])
            noOfPalindromes +=len(uniqueCharacters)
        
        return noOfPalindromes
            
