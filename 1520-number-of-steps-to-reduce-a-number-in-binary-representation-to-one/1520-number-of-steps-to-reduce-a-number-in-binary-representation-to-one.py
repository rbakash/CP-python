class Solution:
    def numSteps(self, s: str) -> int:
        nearest2 = len(s)-1
        numToReach = 2**nearest2
        steps = 0
        num = int(s,2)
        print(num)
        while num != 1:
            if num %2:
                # odd
                num +=1
            else:
                num = num//2
            steps+=1
        return steps
