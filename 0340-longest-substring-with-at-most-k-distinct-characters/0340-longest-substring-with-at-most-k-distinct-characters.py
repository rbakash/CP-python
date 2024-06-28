class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        uniqueCharacterCount, start,maxLength = 0,0,0
        uniqueCharacters = {}
 

        for end,currentCharacter in enumerate(s):

            if currentCharacter not in uniqueCharacters:
                uniqueCharacterCount +=1

            uniqueCharacters[currentCharacter]=1 + uniqueCharacters.get(currentCharacter,0)

            if uniqueCharacterCount > k:
                uniqueCharacters[s[start]]-=1
                if uniqueCharacters[s[start]] ==0:
                    uniqueCharacterCount-=1
                    del uniqueCharacters[s[start]]
                start+=1
            maxLength = max(maxLength, (end-start+1))

        return maxLength