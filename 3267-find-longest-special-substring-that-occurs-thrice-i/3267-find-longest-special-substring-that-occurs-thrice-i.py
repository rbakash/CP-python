class Solution:
    def maximumLength(self, s: str) -> int:

        subStringFrequency = defaultdict(int)
        n = len(s)
        for start in range(n):
            currentCharacter = s[start]
            subStringFrequency[s[start]] += 1
            for end in range(start + 1, n):
                if s[end] != currentCharacter:
                    break
                subStringFrequency[s[start : end + 1]] += 1
            
        # print(subStringFrequency)
        maxLength = 0
        for substring, count in subStringFrequency.items():
            if count >= 3:
                maxLength = max(maxLength, len(substring))
        return maxLength if maxLength != 0 else -1
