class neighborSum:

    def __init__(self, grid: List[List[int]]):
        
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.grid=[[0 for _ in range(self.cols)] for _ in range(self.rows)]
        
        for row in range(self.rows):
            for col in range(self.cols):
                self.grid[row][col]=grid[row][col]

    def findValue(self,value)->(int,int):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == value:
                    return (row,col)
                    
    def adjacentSum(self, value: int) -> int:
        directions = [(0,-1),(0,1),(-1,0),(1,0)]
        valueRow,valueCol = self.findValue(value)
        adjSum=0

        for eachRow,eachCol in directions:
            offSetRow,offSetCol = valueRow+eachRow,valueCol+eachCol
            
            if offSetRow>=0 and  offSetRow < self.rows and offSetCol >=0 and offSetCol < self.cols:
                adjSum+=self.grid[offSetRow][offSetCol]
        
        return adjSum

    def diagonalSum(self, value: int) -> int:
        directions = [(-1,-1),(-1,1),(1,-1),(1,1)]
        valueRow,valueCol = self.findValue(value)
        diagonalSum=0

        for eachRow,eachCol in directions:
            offSetRow,offSetCol = valueRow+eachRow,valueCol+eachCol
            if offSetRow>=0 and  offSetRow < self.rows and offSetCol >=0 and offSetCol < self.cols:
                diagonalSum+=self.grid[offSetRow][offSetCol]
        
        return diagonalSum


# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)