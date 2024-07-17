class Solution:
    def frequencySort(self, s: str) -> str:
        frequency = defaultdict(int)
        for eachCharacter in s:
            frequency[eachCharacter]+=1
        
        string = sorted(frequency.items(), key=lambda x:x[1],reverse = True)
        print(string)
        result = []
        for ch,count in string:
            result.append(ch*count)
        return "".join(result)