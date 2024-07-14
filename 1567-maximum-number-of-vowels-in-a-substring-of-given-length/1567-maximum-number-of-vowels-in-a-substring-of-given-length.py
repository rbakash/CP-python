class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ["a", "e", "i", "o", "u"]
        maxVowels, currentVowels = 0, 0

        for character in s[:k]:
            if character in vowels:
                currentVowels += 1
        maxVowels = currentVowels
        for end in range(k, len(s)):

            if s[end - k] in vowels:
                currentVowels -= 1
            if s[end] in vowels:
                currentVowels += 1
            maxVowels = max(maxVowels, currentVowels)

        return maxVowels
