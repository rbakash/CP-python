class Solution:
    def makesquare(self, matchSticks: List[int]) -> bool:
        eachSide = sum(matchSticks)//4
        length = len(matchSticks)
        if sum(matchSticks)/4 != eachSide:
            return False
        sides=[0]*4
        matchSticks.sort(reverse=True)
        def dfs(currentIndex):
            if currentIndex == length:
                return True
            for sideIndex in range(4):
                if sides[sideIndex] + matchSticks[currentIndex] <= eachSide:
                    sides[sideIndex] += matchSticks[currentIndex]
                    if dfs(currentIndex+1):
                        return True
                    sides[sideIndex] -= matchSticks[currentIndex]
            return False
        return dfs(0)
                    

