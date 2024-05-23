class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        end = 0
        n = len(s)
        frequency = {}
        result = 0

        while end < n:
            # increment the occurence
            frequency[s[end]] = frequency.get(s[end], 0) + 1

            # get the most occuring character
            mostOccuring = max(frequency.values())

            # check if its valid substring
            numberOfReplacement = (end - start + 1) - mostOccuring

            while (end - start + 1) - mostOccuring > k:
                frequency[s[start]] -= 1
                start += 1

            result = max((end - start + 1), result)
            end += 1

        return result
