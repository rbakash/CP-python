class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        # convert to digits
        digits = [int(digit) for digit in str(n)]
        breakingIndex=len(digits)

        # Find the breaking point when monotonic breaks
        for index in range(len(digits)-1,0,-1):
            if digits[index]<digits[index-1]:
                digits[index-1]-=1
                breakingIndex =index

        # replace all the digits with 9 as <= is allowed, 99 is valid and 89 is also valid
        digits[breakingIndex:]=[9]*(len(digits)-breakingIndex)

        # map(str,digits) -> basically converts all the int to str and map basically calls str for each element in digits
        # Alternative is int("".join([str(x) for x in digits])
        return int("".join(map(str, digits)))
                