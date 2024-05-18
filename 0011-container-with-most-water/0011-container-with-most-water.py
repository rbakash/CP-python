class Solution:
    def maxArea(self, height: List[int]) -> int:

        startLine = 0
        maxAmountOfWater = 0
        endLine = len(height) - 1

        while endLine > startLine:
            currentArea = min(height[endLine], height[startLine]) * abs(
                endLine - startLine
            )

            maxAmountOfWater = max(currentArea, maxAmountOfWater)
            if height[endLine] < height[startLine]:
                endLine -= 1
            else:
                startLine += 1

        return maxAmountOfWater
