class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        visited= set()
        directions = [[-1,0],[1,0],[0,-1],[0,1]]

        def dfs(row,col):
            if row <0 or row == rows or col < 0 or col == cols or board[row][col] != "O":
                return
            board[row][col]="T"
            for dr,dc in directions:
                dr,dc = dr+row,dc+col
                dfs(dr,dc)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O" and (row in [0,rows-1] or col in [0,cols-1]):
                    dfs(row,col)
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "T":
                    board[row][col] = "O"