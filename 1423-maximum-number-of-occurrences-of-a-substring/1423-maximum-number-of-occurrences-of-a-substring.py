class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        characterFrequency = defaultdict(int)
        substringFrequency = defaultdict(int)

        start = 0
        maxOccurence,maxOccurringSubString = 0,""
        for end in range(len(s)):

            # expand the window
            if characterFrequency[s[end]] ==0:
                maxLetters -= 1
            characterFrequency[s[end]] += 1

            # shrink the window
            while (end - start+1) >= minSize and (end - start+1) <= maxSize :
                if maxLetters >=0:
                    substringFrequency[s[start : end + 1]] += 1
                    # Find the max occurence
                    if substringFrequency[s[start : end + 1]] > maxOccurence:
                        maxOccurence = substringFrequency[s[start : end + 1]]
                        maxOccurringSubString = s[start : end + 1]
                # if not restore the maxLetter
                characterFrequency[s[start]] -= 1
                if characterFrequency[s[start]] == 0:
                    maxLetters += 1
                
                start += 1

        return maxOccurence
