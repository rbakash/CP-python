# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:


class Solution:
    def findCelebrity(self, n: int) -> int:
        
        def isCelebrity(i):
            for dest in range(n):
                if src != dest:
                    if knows(src,dest) or not knows(dest,src):
                       return False
            return True
        for src in range(n):
            if isCelebrity(src):
                return src
        return -1
