class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = [int(digit) for digit in str(n)]
        breakingIndex=len(digits)
        for index in range(len(digits)-1,0,-1):
            if digits[index]<digits[index-1]:
                digits[index-1]-=1
                breakingIndex =index
        digits[breakingIndex:]=[9]*(len(digits)-breakingIndex)
        return int("".join(map(str, digits)))
                