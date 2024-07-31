class Solution:
    def splitString(self, s: str) -> bool:
        length = len(s)
        def backTrack(currentIndex, noOfParts,previous)->bool:
            if currentIndex == length:
                return noOfParts >=2
            for index in range(currentIndex,length):
                num = int(s[currentIndex:index+1])
                if previous == float("inf") or num == previous-1:
                    if backTrack(index+1,noOfParts+1,num):
                        return True
            return False
        return backTrack(0,0,float("inf"))