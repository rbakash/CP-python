class Solution:
    def maxProduct(self, words: List[str]) -> int:
        maxLength = 0
        n = len(words)
        # compute the bitmasks
        bitmask = [0] * n
        length = [0] * n

        for index in range(n):
            mask = 0
            length[index] = len(words[index])
            for eachCharacter in words[index]:
                mask = mask | (1 << (ord(eachCharacter) - ord("a")))
            bitmask[index] = mask

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if bitmask[j] & bitmask[i] == 0:
                    # No common alphabets
                    maxLength = max(maxLength, length[i] * length[j])

        return maxLength
