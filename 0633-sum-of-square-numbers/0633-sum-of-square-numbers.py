class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        # See if you can make c from numbers till sqrt 
        start,end = 0,ceil(sqrt(c))
        while start <= end:
            square = start**2 + end**2
            if square == c:
                return True
            elif square < c:
                start+=1
            else:
                end-=1

        return False