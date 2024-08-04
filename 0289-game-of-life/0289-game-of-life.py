class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        updates = list()
        rows = len(board)
        cols = len(board[0])
        directions = [
            (0, -1),
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
        ]
        for row in range(rows):
            for col in range(cols):
                noOfLifes = 0
                for offSetRow, offSetCol in directions:
                    newRow, newCol = row + offSetRow, col + offSetCol
                    if (-1 < newRow < rows) and (-1 < newCol < cols) and abs(board[newRow][newCol]) == 1:
                            noOfLifes += 1
                
                if board[row][col] == 1:
                    if noOfLifes<2 or noOfLifes >3:
                        # updates.append((row, col, 0))
                        board[row][col]=-1

                else :
                    if noOfLifes ==3:
                        board[row][col]=2
                        # updates.append((row, col, 1))
                
        print(updates)
        # update the board m*n for each value in updates
        # for row, col, value in updates:
        #     board[row][col] = value
        for row in range(rows):
            for col in range(cols):
                if board[row][col] <=0:
                    board[row][col] =0
                else:
                    board[row][col] =1
        print(board)
        return None
