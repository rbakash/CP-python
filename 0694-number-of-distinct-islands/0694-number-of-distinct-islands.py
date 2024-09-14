class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        uniquePaths = set()
        visited = set()
        paths = {
            (0,1):"R",
            (1,0):"D",
            (0,-1):"L",
            (-1,0):"T"
        }

        def dfs(currentRow,currentCol):
            if currentRow<0 or currentRow >=rows or currentCol<0 or currentCol>=cols :
                return 
            if grid[currentRow][currentCol]==0 or (currentRow,currentCol) in visited:
                return
            visited.add((currentRow,currentCol))
            for (rowOffset,colOffset), move in paths.items():
                newRow,newCol = currentRow+rowOffset,currentCol+colOffset
                if 0<=newRow<rows and 0<=newCol <cols and grid[newRow][newCol] ==1 and (newRow,newCol) not in visited:
                    self.pathSignature+=move
                    dfs(newRow,newCol)
                self.pathSignature+="#"
            return 
        self.pathSignature = ""
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] ==1 and (row,col) not in visited:
                    self.pathSignature = "#"
                    dfs(row,col)
                    if self.pathSignature != "#":
                        uniquePaths.add(self.pathSignature)

        return len(uniquePaths)