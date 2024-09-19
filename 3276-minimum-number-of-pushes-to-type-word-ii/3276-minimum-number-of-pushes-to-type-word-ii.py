class Solution:
    def minimumPushes(self, word: str) -> int:
        # sort by frequency then count the pushes
        freq = defaultdict(int)
        for char in word:
            freq[char]+=1
        sortedFreq = sorted(freq.items(), key=lambda x:-x[1])
        print(sortedFreq)
        minPushes =0
        currentPress,currentChar =1,1
        for char,count in sortedFreq:
            if currentChar >8:
                currentPress +=1
                currentChar = 1
            minPushes += (count * currentPress)
            currentChar+=1
        return minPushes
        