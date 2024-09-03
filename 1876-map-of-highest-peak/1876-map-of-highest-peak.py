class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        queue = deque()
        visited = set()
        height = [[-1]*len(isWater[0]) for _ in range(len(isWater))]
        directions = [(0,-1),(-1,0),(0,1),(1,0)]

        # Add all the water
        for currentRow in range(len(isWater)):
            for currentCol in range(len(isWater[0])):
                if isWater[currentRow][currentCol] == 1:
                    queue.append((currentRow,currentCol,0)) # row,col, currentHeight
                    height[currentRow][currentCol]=0
        
        # Multiple source BFS
        while queue:
            currentLevel = len(queue)
            minHeight =0
            # for index in range(currentLevel):
            currentRow,currentCol,currentHeight = queue.popleft()
            for rowOffset,colOffset in directions:
                newRow,newCol = currentRow + rowOffset, currentCol + colOffset
                if  0 <= newRow <len(isWater) and 0<= newCol < len(isWater[0]) and height[newRow][newCol]==-1:
                    # if this is not visited, then add
                    visited.add((newRow,newCol))
                    height[newRow][newCol]=height[currentRow][currentCol]+1
                    queue.append((newRow,newCol,currentHeight+1))
        return height
