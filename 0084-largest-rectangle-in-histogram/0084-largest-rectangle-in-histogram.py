class Solution:
    def largestRectangleAreaBrute(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea =0
   
        for left in range(n):
            currentMin = heights[left]
            for right in range(left,n):
                if heights[right]<currentMin:
                    currentMin = heights[right]
                currentArea = currentMin * (right-left+1)
                if currentArea > maxArea:
                    maxArea = currentArea
            print(maxArea)
        return maxArea
    def largestRectangleAreaDivideConquer(self, heights: List[int]) -> int:
        def calculateArea(start,end)->int:
            if start > end:
                return 0
            minIndex = start
            for index in range(start,end+1):
                if heights[index]< heights[minIndex]:
                    minIndex = index
            maxArea = max(
                heights[minIndex]*(end-start+1),
                calculateArea(start,minIndex-1),
                calculateArea(minIndex+1,end)
            )
            return maxArea
        return calculateArea(0,len(heights)-1)

    def largestRectangleArea(self, height: List[int]) -> int:
        height.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        height.pop()
        return ans    