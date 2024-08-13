class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        freq=defaultdict(int)
        left =0
        for right in range(len(s)+1):
            if right-left ==10:
                freq[s[left:right]]+=1
                left+=1
        print(freq)
        result=[]

        for substring, count in freq.items():
            if count>1:
                result.append(substring)
        
        return result