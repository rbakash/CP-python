class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        freqOfBrackets = defaultdict(list)
        for index in range(len(s)):
            if s[index] in ["(", ")"]:
                freqOfBrackets[s[index]].append(index)

        pointerO, pointerC = 0, 0
        indexesToDelete = set()
        print(freqOfBrackets)
        while pointerO < len(freqOfBrackets["("]) and pointerC < len(freqOfBrackets[")"]):
            print(freqOfBrackets[")"][pointerC], freqOfBrackets[")"][pointerO])
            if freqOfBrackets[")"][pointerC] < freqOfBrackets["("][pointerO]:
                print(s[freqOfBrackets[")"][pointerC]])
                # invalid Close bracket, we need to remove it tp make it valid
                indexesToDelete.add(freqOfBrackets[")"][pointerC])
                pointerC += 1
            else:
                pointerO += 1
                pointerC += 1

        print(s, pointerO, pointerC, pointerO < len(freqOfBrackets["("]))
        # remove remaining invalid brackets
        while pointerO < len(freqOfBrackets["("]):
            indexesToDelete.add(freqOfBrackets["("][pointerO])
            pointerO += 1

        while pointerC < len(freqOfBrackets[")"]):
            indexesToDelete.add(freqOfBrackets[")"][pointerC])
            pointerC += 1
        result = ""
        for index in range(len(s)):
            if index not in indexesToDelete:
                result += s[index]
        return result
