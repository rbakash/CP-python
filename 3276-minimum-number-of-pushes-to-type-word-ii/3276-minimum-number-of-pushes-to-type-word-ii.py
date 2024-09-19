class Solution:
    def minimumPushes(self, word: str) -> int:
        # sort by frequency then count the pushes
        freq = defaultdict(int)
        for char in word:
            freq[char]+=1
        sortedFreq = sorted(freq.items(), key=lambda x:-x[1])
        
        minPushes =0
        currentPress,currentChar =1,1
        for char,count in sortedFreq:
            if currentChar >8:
                currentPress +=1
                currentChar = 1
            minPushes += (count * currentPress)
            currentChar+=1

        # Other easy solution - sum the number series 1* sum[:8] + 2* sum([8:16]) & so on
        sortedFreq = [ x[1] for x in sortedFreq]
        totalPush = sum(sortedFreq[:8]) + 2*sum(sortedFreq[8:16]) + 3 * sum(sortedFreq[16:24]) + 4* sum(sortedFreq[24:32])
        
        return totalPush
        