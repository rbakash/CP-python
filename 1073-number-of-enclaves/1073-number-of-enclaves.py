class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        numberOfEnclaves = 0
        direction = [(0,-1),(0,1),(-1,0),(1,0)]

        def dfs(currentRow,currentColumn):
            if  grid[currentRow][currentColumn]==0:
                return
            grid[currentRow][currentColumn]=0
            for rowOffset,colOffset in direction:
                newRow,newColumn =  currentRow+rowOffset, currentColumn + colOffset
                if newRow >=0 and newRow < rows and newColumn >= 0 and newColumn < columns:
                    dfs(newRow,newColumn)
            return

        for row in range(rows):
            for col in range(columns):
                if (row in [0,rows-1] or col in [0,columns-1]) and grid[row][col]==1:
                    dfs(row,col)
        for row in range(rows):
            for col in range(columns):
                if grid[row][col] ==1:
                    numberOfEnclaves+=1
        return numberOfEnclaves

