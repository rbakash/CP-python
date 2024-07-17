class Solution:
    def frequencySort(self, s: str) -> str:
        frequency = defaultdict(int)
        for eachCharacter in s:
            frequency[eachCharacter]+=1
        
        string = sorted(frequency.items(), key=lambda x:x[1],reverse = True)
        result = ""
        for ch,count in string:
            result+=ch*count
        return result