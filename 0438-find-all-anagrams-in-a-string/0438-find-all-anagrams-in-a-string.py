class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        stringSLength = len(s)
        stringPLength = len(p)
        if stringSLength < stringPLength:
            return []

        anagramIndex = []
        stringSFrequency, stringPFrequency = [0] * 26, [0] * 26

        # create frequency map
        for index in range(stringPLength):
            stringPFrequency[ord(p[index]) - ord("a")] += 1

        for index in range(stringSLength):

            stringSFrequency[ord(s[index]) - ord("a")] += 1
            if index >= stringPLength:

                stringSFrequency[ord(s[index - stringPLength]) - ord("a")] -= 1

            if stringSFrequency == stringPFrequency:
                anagramIndex.append(index - stringPLength + 1)

        return anagramIndex
