class Solution:
    def customSortString(self, order: str, s: str) -> str:

        frequency  = {}
        for each in s:
            frequency[each]= frequency.get(each,0 ) +1
        
        result=""

        for eachCharacter in order:
            if eachCharacter in frequency:
                result+=(eachCharacter * frequency[eachCharacter])
                del frequency[eachCharacter]
        
        for char, count in frequency.items():
            result+=(char * count)
        
        return result
        
