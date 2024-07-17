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

        matching_subseq_count = 0
        for word in words:
            current_index = -1
            for char in word:
                current_index = s.find(char, current_index + 1)
                if current_index == -1:
                    break
            if current_index != -1:
                matching_subseq_count += 1
        return matching_subseq_count
