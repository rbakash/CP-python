class Solution:
    def minimumKeypresses(self, s: str) -> int:
        n = len(s)
        # You can distribute each key per number
        if n <= 9:
            return n
        keyPresses = 0

        frequency = defaultdict(int)
        for eachCharacter in s:
            frequency[eachCharacter] += 1
        sortedList = sorted(frequency.values(), reverse=True)
        # n-=9
        iterator = 0
        for idx, value in enumerate(sortedList):

            iterator = iterator + 1 if idx % 9 == 0 else iterator
            keyPresses += value * iterator
        return keyPresses