class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dimension = 9
        rowsSet = [set() for _ in range(dimension)]
        colsSet = [set() for _ in range(dimension)]
        # colSet = Set() * dimension 
        boxSet = [set() for row in range(dimension)]
        
        print(rowsSet)
        print(boxSet)
        for row in range(0, len(board)):
            for column in range(0,len(board[row])):
                if board[row][column] != ".":
                    if board[row][column] in rowsSet[row]:
                        return False
                    rowsSet[row].add(board[row][column])
                    if board[row][column] in colsSet[column]:
                        return False
                    colsSet[column].add(board[row][column])
                    index = (row//3) * 3 + (column //3 )
                    if board[row][column] in boxSet[index]:
                        return False
                    boxSet[index].add(board[row][column])

        return True