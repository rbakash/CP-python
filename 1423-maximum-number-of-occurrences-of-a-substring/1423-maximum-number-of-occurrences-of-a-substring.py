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

        # Optimal fuck
        # If you think about the nature of substrings, any substring of size n must be made up of substrings of size n-1 + a single character. 
        # Therefore, you can see that the maximum occurrence of a substring of size n is <= the maximum occurrence of a substring of size n-1.
        # So you do not need to check any substrings of size maxSize, only minSize which will give you the maximum answer.

        # lookup = defaultdict(int)
        # maxOccurence, maxOccurringSubString = 0, ""
        # def isValidSubstring(substring: str) -> bool:
        #     return len(set(substring) )<= maxLetters

        # for i in range(minSize, len(s)+1):
        #     subarray = s[i-minSize:i]

        #     if isValidSubstring(subarray):
        #         lookup[subarray] += 1
        #         if lookup[subarray] > maxOccurence:
        #             maxOccurence = lookup[subarray]
        #             maxOccurringSubString = subarray
        # return maxOccurence

