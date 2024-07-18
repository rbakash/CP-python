class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        freqOfBrackets = defaultdict(list)
        for index in range(len(s)):
            if s[index] in ["(", ")"]:
                freqOfBrackets[s[index]].append(index)

        pointerO, pointerC = 0, 0
        indexesToDelete = set()

        while pointerO < len(freqOfBrackets["("]) and pointerC < len(freqOfBrackets[")"]):
            
            if freqOfBrackets[")"][pointerC] < freqOfBrackets["("][pointerO]:

                # invalid Close bracket, we need to remove it tp make it valid
                indexesToDelete.add(freqOfBrackets[")"][pointerC])
                pointerC += 1
            else:
                pointerO += 1
                pointerC += 1

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
