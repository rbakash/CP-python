class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # impossible to create k palindromes if its more than len(s)
        if k > len(s):
            return False
        
        # find the character with odd frequency
        frequency = defaultdict(int)
        for character in s:
            frequency[character]+=1
        oddFrequency =0
        
        for character,count in frequency.items():
            if count % 2 == 1:
                oddFrequency+=1

        # We can create at most oddFrequency palindromes 
        # as each odd frequency character need to be in seperate palindrome
        # Ex : aabc, a = 2, b =1 , c = 1,
        # palindromes can be aba, aca so you can create minimum of 2 palindromes
        if oddFrequency <=  k:
            return True
        else:
            return False