class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        wordMap = defaultdict(list)
        for index, word in enumerate(dictionary):
            wordMap[word[0]].append((word, word))
        longestWord = ""

        for character in s:
            currentWords = wordMap[character]
            wordMap[character]=[]
            for eachWord, actualDict in currentWords:
                if len(eachWord) == 1:

                    if len(longestWord) == len(actualDict) and actualDict < longestWord:
                        longestWord = actualDict
                    elif len(longestWord) < len(actualDict):
                        longestWord = actualDict
                else:
                    wordMap[eachWord[1]].append((eachWord[1:], actualDict))

        return longestWord
