class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def isSubsequence(target):
            sourcePointer, targetPointer = 0, 0
            while targetPointer < len(target) and sourcePointer < len(s):
                if s[sourcePointer] == target[targetPointer]:
                    targetPointer += 1
                sourcePointer += 1
            return targetPointer == len(target)

        # matchingSubsequence = 0
        # for word in words:
        #     if isSubsequence(word):
        #         matchingSubsequence += 1

        # this is next Level logic as stated in editorial, idk how it works
        # wordCharacterMap=defaultdict(list)
        # matchingSubsequence = 0
        # for word in words:
        #     wordCharacterMap[word[0]].append(word)

        # for character in s:
        #     currentWords = wordCharacterMap[character]
        #     wordCharacterMap[character] = []

        #     for eachWord in currentWords:
        #         if len(eachWord) ==1:
        #             matchingSubsequence += 1
        #         else:
        #             wordCharacterMap[eachWord[1]].append(eachWord[1:])

        # return matchingSubsequence

        # extremely simple logic - brute force
        matchingSubsequence = 0
        for word in words:
            currentIndex = -1
            # check if all the character in the given word exists or not
            # if exists then its a matching subsequence
            for eachCharacter in word:
                # s.find -> finds the character starting from currentIndex +1,returns the index if found else -1
                currentIndex = s.find(eachCharacter, currentIndex + 1)
                if currentIndex == -1:
                    break
            if currentIndex != -1:
                matchingSubsequence += 1
        return matchingSubsequence
