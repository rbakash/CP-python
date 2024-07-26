class Solution:
    def makesquare(self, matchSticks: List[int]) -> bool:
        eachSide = sum(matchSticks)
        if eachSide % 4 != 0:
            return False
        eachSide = eachSide // 4
        length = len(matchSticks)
        
        sides = [0] * 4
        # no point to start with smaller matchsticks
        matchSticks.sort(reverse=True)

        def dfs(currentIndex):
            # if no matchstick is left to add
            if currentIndex == length:
                return True
            # try to fit the current match stick in all the 4 side and see if it fits
            for sideIndex in range(4):
                # if the current length is greater than sum(match)//4, then no point in continuing
                if sides[sideIndex] + matchSticks[currentIndex] > eachSide:
                    continue
                # Try to add to smaller side and we can avoid adding to equal sides
                if sideIndex > 0 and sides[sideIndex] == sides[sideIndex-1]:
                    continue
                # if the sum is less then, we can add more match sticks
                if sides[sideIndex] + matchSticks[currentIndex] <= eachSide:
                    sides[sideIndex] += matchSticks[currentIndex]
                    # If we made all the match stick equal
                    if dfs(currentIndex + 1):
                        return True
                    sides[sideIndex] -= matchSticks[currentIndex]
            return False

        return dfs(0)
