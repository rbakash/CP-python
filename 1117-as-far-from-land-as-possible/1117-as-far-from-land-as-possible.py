class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        maxDistance,currentDistance=0,0
        queue=deque() # currentIndex,  startedFrom Index     
        visited = set()
        directions=[(-1,0),(1,0),(0,-1),(0,1)]

        # add all Land(1's) to queue
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    queue.append((row,col))
                    visited.add((row,col))
        
        # If there are no land cells or only land cells, handle that case
        if len(queue) == 0 or len(queue) == len(grid) * len(grid[0]):
            return -1

        while queue:
            currentLevel = len(queue)
            # all the neighboring cells
            for level in range(currentLevel):
                currentRow,currentCol = queue.popleft()
                
                for rowOffset,colOffset in directions:
                    newRow,newCol = currentRow+rowOffset, currentCol + colOffset
                    if (0<= newRow<len(grid) and 0<=newCol<len(grid[0])) and (newRow,newCol) not in visited:
                        visited.add((newRow,newCol))
                        queue.append((newRow,newCol))
            currentDistance+=1

        return currentDistance -1
        