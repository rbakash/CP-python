class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # orderChar=set([charac for charac in order])
        sChar=set([charac for charac in s])
        frequency  = defaultdict(int)
        for each in s:
            frequency[each]+=1

        result=[]
        print(frequency)
        print(sChar)

        for eachCharacter in order:
            if eachCharacter in frequency:
                for count in range(frequency[eachCharacter]):
                    result.append(eachCharacter)
                del frequency[eachCharacter]
        
        for char, count in frequency.items():
            for count in range(count):
                result.append(char)
        
        return "".join(result)
        
