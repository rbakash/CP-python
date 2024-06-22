class Solution:
    def customSortString(self, order: str, s: str) -> str:
        sChar=set([charac for charac in s])
        frequency  = defaultdict(int)
        for each in s:
            frequency[each]+=1
        result=""

        for eachCharacter in order:
            if eachCharacter in frequency:
                result+=(eachCharacter * frequency[eachCharacter])
                del frequency[eachCharacter]
        
        for char, count in frequency.items():
            result+=(char * count)
        
        return result
        
