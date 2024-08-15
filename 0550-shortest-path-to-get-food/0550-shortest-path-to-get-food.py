class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        directions=[(0,-1),(0,1),(-1,0),(1,0)]
        rows,cols = len(grid),len(grid[0])
        visited = set()
        startingRow,startingCol = -1,-1

        # find the src
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "*":
                    startingRow,startingCol = row,col
                    break
        minHeap=[[0,startingRow,startingCol]]
        while minHeap:
            currentCost,currentRow,currentCol = heappop(minHeap)
            if grid[currentRow][currentCol] =="#":
                return currentCost

            for rowOffset,colOffset in directions:
                newRow,newCol = currentRow+rowOffset,currentCol+colOffset
                if 0<=newRow<rows and 0<=newCol<cols and (newRow,newCol) not in visited:
                    visited.add((newRow,newCol))
                    if grid[newRow][newCol] in ["O","#"]:
                        heappush(minHeap,(currentCost+1,newRow,newCol))
        return -1