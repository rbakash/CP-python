class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacificOcean=set()
        altlanticOcean = set()
        directions = [[-1,0],[1,0],[0,-1],[0,1]]

        def dfs(row,col,visited,prevHeight):
            if row < 0 or row == rows or col < 0 or col== cols or (row,col) in visited or heights[row][col] < prevHeight:
                return
            visited.add((row,col))
            for dr,dc in directions:
                dr,dc = row+dr,col+dc
                dfs(dr,dc,visited,heights[row][col])

        for col in range(cols):
            dfs(0,col,pacificOcean,heights[0][col])
            dfs(rows-1,col,altlanticOcean,heights[rows-1][col])

        for row in range(rows):
            dfs(row,0,pacificOcean,heights[row][0])
            dfs(row,cols-1,altlanticOcean,heights[row][cols-1])

        return list(altlanticOcean.intersection(pacificOcean))
