# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:


class Solution:
    def findCelebrity(self, n: int) -> int:
        celebrity = 0
        for src in range(1, n):
            if knows(celebrity, src):
                # if celebrity knows a person, then we can eliminate him
                # as celebrity knows no one
                celebrity = src

        for dest in range(n):
            if celebrity != dest:
                if knows(celebrity, dest) or not knows(dest, celebrity):
                    return -1
        return celebrity
