class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        # maxOccurence, maxOccurringSubString = 0, ""
        # substringFrequency = defaultdict(int)

        # def isValidSubstring(substring: str) -> bool:
        #     return len(set(substring) )<= maxLetters

        # for currentSize in range(minSize, maxSize + 1):
        #     for index in range(len(s) - currentSize + 1):
        #         subString = s[index : index + currentSize]
        #         if isValidSubstring(subString):
        #             substringFrequency[subString] += 1
        #             if substringFrequency[subString] > maxOccurence:
        #                 maxOccurence = substringFrequency[subString]
        #                 maxOccurringSubString = subString

        # return maxOccurence
        lookup = defaultdict(int)

        for i in range(minSize, len(s)+1):
            subarray = s[i-minSize:i]

            if len(set(subarray)) <= maxLetters:
                lookup[subarray] += 1
        
        if lookup:
            return max(lookup.values())
        else:
            return 0
