class Solution:
    def numSteps(self, s: str) -> int:
        s=list(s)
        steps=0

        while len(s) >1:
            if s[-1] =="0":
                # Even, divide by 2
                s.pop()
            else:
                # Odd, add one
                num = int("".join(s),2)
                s=bin(num+1)[2:]
                s=list(s)
            steps+=1
        return steps
