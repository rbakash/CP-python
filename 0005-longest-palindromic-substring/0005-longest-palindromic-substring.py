class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestPalindrome = ""
        n = len(s)
        maxLen = 0

        for index in range(n):
            left = right = index
            while left >= 0 and right < n and s[left] == s[right]:

                if right - left + 1 > maxLen:
                    longestPalindrome = s[left : right + 1]
                    maxLen = right - left + 1
                left -= 1
                right += 1
            left = index
            right = index + 1
            while left >= 0 and right < n and s[left] == s[right]:

                if right - left + 1 > maxLen:
                    longestPalindrome = s[left : right + 1]
                    maxLen = right - left + 1
                left -= 1
                right += 1
        return longestPalindrome
