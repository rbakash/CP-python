class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack =[]
        for digit in num:
            while stack and k and stack[-1]>digit:
                k-=1
                stack.pop()
            stack.append(digit)
        
        # remove the last k for monotnoic increasing stack
        stack = stack[:-k] if k> 0 else stack

        # strip the leading 0
        result = "".join(stack).lstrip('0')

        return result if result else '0'
        