class Solution:
    def myAtoi(self, s: str) -> int:
        result = ""
        sign = 1
        index = 0

        s = s.lstrip(" ")
        if not s:
            return 0

        if s[0] == "+":
            index += 1
            sign = 1
        elif s[0] == "-":
            sign = -1
            index += 1

        for itx in range(index, len(s)):
            if s[itx].isdigit():
                result += s[itx]
            else:
                break
        if result == "" or result in "-+":
            return 0
        elif int(result) > (2**31) - 1:
            return (2**31) - 1
        elif int(result) < -(2**31):
            return -(2**31)
        else:
            return sign * int(result)
