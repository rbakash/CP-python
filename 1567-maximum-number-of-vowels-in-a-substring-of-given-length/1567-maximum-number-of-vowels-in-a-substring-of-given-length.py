class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=['a','e', 'i', 'o','u']
        def countVowels(string:str)->int:
            vowels=['a','e', 'i', 'o','u']
            noOfvowels =0
            for character in string:
                if character in vowels:
                    noOfvowels+=1
            return noOfvowels
        
        maxVowels,start =0,0
        currentVowels = countVowels(s[:k])
        maxVowels = currentVowels
        for end in range(k, len(s)):
            # maxVowels = max(maxVowels, countVowels(s[end:end+k]))
            if s[end-k] in vowels:
                currentVowels-=1
            if s[end] in vowels:
                currentVowels+=1
            maxVowels = max(maxVowels, currentVowels)

        return maxVowels