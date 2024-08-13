class Solution:
    def countPalindromicSubsequenceConstantSpace(self, s: str) -> int:
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
    # Using find and rfind
    def countPalindromicSubsequence(self, s: str) -> int:
        noOfPalindromes = 0
        for char in set(s):
            leftOccurence = s.find(char)
            rightOccurence = s.rfind(char)
            uniqueCharacters=set(s[leftOccurence+1:rightOccurence])
            noOfPalindromes +=len(uniqueCharacters)
        return noOfPalindromes