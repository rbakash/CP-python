class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        maxUniqueCharacter = len(set(s))
        n = len(s)
        maxLength = 0

        for currentUniqueMax in range(1, maxUniqueCharacter + 1):
            # given unique character, find the longest subarray
            frequency = defaultdict(int)
            noOfCharAtLeastKtimes, end = 0, 0
            currentUnique, start = 0, 0
            while end < n:
                # expand the window based on currentUniuq character

                if currentUnique <= currentUniqueMax:
                    if frequency[s[end]] == 0:
                        currentUnique += 1
                    frequency[s[end]] += 1
                    if frequency[s[end]] == k:
                        noOfCharAtLeastKtimes += 1
                    end += 1
                else:

                    while currentUnique > currentUniqueMax:
                        if frequency[s[start]] == k:
                            noOfCharAtLeastKtimes -= 1
                        frequency[s[start]] -= 1
                        if frequency[s[start]] == 0:
                            currentUnique -= 1
                        start += 1
                    print(frequency)
                    print(noOfCharAtLeastKtimes, currentUnique)
                if (
                    currentUnique == currentUniqueMax
                    and currentUnique == noOfCharAtLeastKtimes
                ):
                    print(end, start)
                    maxLength = max(end - start, maxLength)

        return maxLength
