class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        directions=[(0,-1),(0,1),(-1,0),(1,0)]
        rows,cols = len(grid),len(grid[0])
        queue=deque([(grid[0][0],0,0,0)]) # obstacles,steps,row,col
        visited = set()
        
        while queue:
            currentObstacles,currentWeight,currentRow,currentCol = queue.popleft()
            if (currentRow,currentCol) == (rows-1,cols-1):
                return currentWeight
            
            for rowOffset,colOffset in directions:
                newRow,newCol = currentRow+rowOffset,currentCol+colOffset
                if 0<=newRow< rows and 0<=newCol <cols :
                    newObstacles = currentObstacles + grid[newRow][newCol]
                    if newObstacles <= k and (newRow,newCol,newObstacles) not in visited:
                        visited.add((newRow,newCol,newObstacles))
                        queue.append((newObstacles,currentWeight+1,newRow,newCol))
        return -1
            