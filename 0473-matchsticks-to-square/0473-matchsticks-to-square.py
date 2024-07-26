class Solution:
    def makesquare(self, matchSticks: List[int]) -> bool:
        eachSide = sum(matchSticks)
        if eachSide % 4 != 0:
            return False
        eachSide = eachSide // 4
        length = len(matchSticks)
        
        sides = [0] * 4
        matchSticks.sort(reverse=True)

        def dfs(currentIndex):
            if currentIndex == length:
                return True
            for sideIndex in range(4):
                if sides[sideIndex] + matchSticks[currentIndex] > eachSide:
                    continue
                if sideIndex > 0 and sides[sideIndex] == sides[sideIndex-1]:
                    continue
                
                if sides[sideIndex] + matchSticks[currentIndex] <= eachSide:
                    sides[sideIndex] += matchSticks[currentIndex]
                    if dfs(currentIndex + 1):
                        return True
                    sides[sideIndex] -= matchSticks[currentIndex]
            return False

        return dfs(0)
