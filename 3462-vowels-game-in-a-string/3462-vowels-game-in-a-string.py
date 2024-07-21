class Solution:
    def doesAliceWin(self, s: str) -> bool:
        # totalVowels,totalConsonents  = 0,0
        # s=list(s)
         # find Vowel and non vowel count
        for character in s:
            if character in ['a','e', 'i', 'o','u']:
                return True
            # else:
            #     totalConsonents+=1

        return False
        
        # aliceTurn = True

        # while not s:
        #     currentVowelCount,currentConsonentCount = totalVowels, totalConsonents
        #     end = len(s)-1
        #     if aliceTurn:
        #         # find the max Vowel
        #         while currentVowelCount % 2 ==0:
        #             if s[end] in ['a','e', 'i', 'o','u']:
        #                 currentVowelCount-=1
        #             else:
        #                 currentConsonentCount-=1
        #             end-=1
        #         if end == len(s):
        #             s=[]
        #             return True
        #         else:
        #             s=s[end+1:]
        #     else : 
        #         # Bob turn
        #         if totalVowels %2 == 1:
        #             # find the first consonent
        #             start = 0
        #             while s[start] in ['a','e', 'i', 'o','u']:
        #                 start+=1
        #             s.remove(start)
        #             currentConsonentCount-=1

        #     totalVowels = totalVowels - currentVowelCount
        #     totalConsonents = totalConsonents - currentConsonentCount
        #     aliceTurn = not aliceTurn
        # return  aliceTurn       

        