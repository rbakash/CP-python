class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        start = end = 0
        characterFrequency = Counter()
        maximumLength = 0

        while end < len(s):
            # add the character frequency
            characterFrequency[s[end]] += 1

            # after adding the current Element, remove the repeating character if any
            while characterFrequency[s[end]] > 1:
                characterFrequency[s[start]] -= 1
                start += 1

            # Compare the max length if no repeating character
            maximumLength = max(maximumLength, (end - start + 1))
            end += 1
        return maximumLength


# time complexity O(n3) & space is size of substringSet --> O(min(size of string, size of charSet))
