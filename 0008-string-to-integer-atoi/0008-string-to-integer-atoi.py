class Solution:
    def myAtoi(self, s: str) -> int:
        result = 0
        sign = 1
        index=0
        INT_MAX = (2**31)-1
        INT_MIN = -(2**31)

        s = s.lstrip(" ")
        if not s:
            return 0
        if s[0] =="+":
            index +=1
            sign =1
        elif s[0] =="-":
            sign=-1
            index+=1
        while index< len(s) and s[index].isdigit():
            digit = int(s[index])
            # Check if we can add digit to result by comparing result and int max till last digit
            if (result > INT_MAX//10) or (result == INT_MAX//10 and digit > INT_MAX%10):
                return INT_MAX if sign == 1 else INT_MIN

            result = result*10 + digit 
            index+=1
    
        return sign * result
