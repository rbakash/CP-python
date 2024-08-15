class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        directions=[(0,-1),(0,1),(-1,0),(1,0)]
        rows,cols = len(grid),len(grid[0])
        startingRow,startingCol = -1,-1

        # find the src
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "*":
                    startingRow,startingCol = row,col
                    break
        
        minHeap=deque([(0,startingRow,startingCol)])
        
        while minHeap:
            currentCost,currentRow,currentCol = minHeap.popleft()
            if grid[currentRow][currentCol] =="#":
                return currentCost

            for rowOffset,colOffset in directions:
                newRow,newCol = currentRow+rowOffset,currentCol+colOffset
                if 0<=newRow<rows and 0<=newCol<cols and grid[newRow][newCol] !="X":
                    # mark as X so we don't visit it again
                    grid[newRow][newCol]='X' if grid[newRow][newCol]!='#' else '#'
                    minHeap.append((currentCost+1,newRow,newCol))
        return -1