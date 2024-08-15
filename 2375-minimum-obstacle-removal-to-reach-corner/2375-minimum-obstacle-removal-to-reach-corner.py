class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        visited=set()
        minHeap=[(grid[0][0], grid[0][0],0,0)] # weight,noOfblockages, row,col
        directions = [(0,-1),(0,1),(-1,0),(1,0)] # 4 directions
        rows,cols = len(grid),len(grid[0])
        
        while minHeap:
            currentWeight,currentBlockages, currentRow,currentCol = heappop(minHeap)
            if (currentRow,currentCol) == (rows-1,cols-1):
                return currentBlockages
            if (currentRow,currentCol) in visited:
                continue
            visited.add((currentRow,currentCol))
            for rowOffset,colOffset in directions:
                newRow,newCol = currentRow+rowOffset,currentCol+colOffset
                if 0<=newRow<rows and 0<=newCol<cols and (newRow,newCol) not in visited:
                    heappush(minHeap, (grid[newRow][newCol],currentBlockages+grid[newRow][newCol],newRow,newCol))
        return -1