class Solution:
    def myAtoi(self, s: str) -> int:
        result = 0
        sign = 1
        index = 0

        s = s.lstrip(" ")
        if not s:
            return 0

        if s[0] == "+":
            sign = 1
            s=s[1:]
        elif s[0] == "-":
            sign = -1
            s=s[1:]

        for itx in range(len(s)):
            if s[itx].isnumeric():
                result = result*10 + int(s[itx])
            else:
                break
        if result == 0:
            return 0
        
        result = sign * (result)
        if result > (2**31) - 1:
            return (2**31) - 1
        elif result < -(2**31):
            return -(2**31)
        else:
            return result
