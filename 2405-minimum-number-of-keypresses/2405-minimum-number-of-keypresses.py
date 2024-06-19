class Solution:
    def minimumKeypresses(self, s: str) -> int:
        n = len(s)
        keypad=defaultdict(list)
        # You can distribute each key per number
        if n <= 9:
            return n

        keyPresses, iterator = 0, 0
        frequency = defaultdict(int)

        for eachCharacter in s:
            frequency[eachCharacter] += 1
        sortedList = sorted(frequency.items(),key= lambda item:item[1], reverse=True)

        for idx, (char,occurence) in enumerate(sortedList):

            iterator = iterator + 1 if idx % 9 == 0 else iterator
            keyPresses += occurence * iterator
            keypad[(idx+1)%9].append(char)
        print(keypad)
        return keyPresses
