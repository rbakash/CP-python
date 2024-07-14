class Solution:
    def getSmallestString(self, s: str) -> str:
        digits = [int(digit)  for digit in s]
        count=0

        for index in range(1,len(s)):
            if digits[index-1]%2 == digits[index]%2 and digits[index] < digits[index-1] and count <1:
                count+=1
                digits[index],digits[index-1]=digits[index-1],digits[index]
       

        return "".join(map(str,digits))