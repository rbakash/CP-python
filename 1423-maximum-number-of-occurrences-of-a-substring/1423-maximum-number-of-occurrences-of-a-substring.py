class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        maxOccurence, maxOccurringSubString = 0, ""
        substringFrequency = defaultdict(int)

        def isValidSubstring(substring: str) -> bool:
            return len(set(substring) )<= maxLetters

        for currentSize in range(minSize, maxSize + 1):
            for index in range(len(s) - currentSize + 1):
                subString = s[index : index + currentSize]
                if isValidSubstring(subString):
                    substringFrequency[subString] += 1
                    if substringFrequency[subString] > maxOccurence:
                        maxOccurence = substringFrequency[subString]
                        maxOccurringSubString = subString

        # start, uniqueCharacters = 0, 0
        # for end in range(len(s)):

        #     # expand the window
        #     if s[end] not in characterFrequency:
        #         uniqueCharacters += 1
        #     characterFrequency[s[end]] += 1

        #     if (end - start)+1 >= minSize:
        #         if (end - start)+1 > maxSize or uniqueCharacters > maxLetters:
        #             # shrink the window
        #             while (end - start)+1 > maxSize or uniqueCharacters > maxLetters:
        #                 characterFrequency[s[start]] -= 1
        #                 if characterFrequency[s[start]] == 0:
        #                     uniqueCharacters -= 1
        #                     del characterFrequency[s[start]]
        #                 start += 1
        #             if (end - start)+1 >= minSize:
        #                 substringFrequency[s[start : end + 1]] += 1
        #         else:
        #             # valid string if maxLetter
        #             substringFrequency[s[start : end + 1]] += 1

        # for substring,count in substringFrequency.items():

        return maxOccurence
