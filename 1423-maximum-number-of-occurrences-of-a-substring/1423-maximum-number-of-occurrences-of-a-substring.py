class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        # maxOccurence, maxOccurringSubString = 0, ""
        # substringFrequency = defaultdict(int)

        

        # for currentSize in range(minSize, maxSize + 1):
        #     for index in range(len(s) - currentSize + 1):
        #         subString = s[index : index + currentSize]
        #         if isValidSubstring(subString):
        #             substringFrequency[subString] += 1
        #             if substringFrequency[subString] > maxOccurence:
        #                 maxOccurence = substringFrequency[subString]
        #                 maxOccurringSubString = subString

        # return maxOccurence

        # Optimal fuck
        # If you think about the nature of substrings, any substring of size n must be made up of substrings of size n-1 + a single character. 
        # Therefore, you can see that the maximum occurrence of a substring of size n is <= the maximum occurrence of a substring of size n-1.
        # So you do not need to check any substrings of size maxSize, only minSize which will give you the maximum answer.

        lookup = defaultdict(int)
        maxOccurence, maxOccurringSubString = 0, ""
        def isValidSubstring(substring: str) -> bool:
            return len(set(substring) )<= maxLetters

        for i in range(minSize, len(s)+1):
            subarray = s[i-minSize:i]

            if isValidSubstring(subarray):
                lookup[subarray] += 1
                if lookup[subarray] > maxOccurence:
                    maxOccurence = lookup[subarray]
                    maxOccurringSubString = subarray
        return maxOccurence
