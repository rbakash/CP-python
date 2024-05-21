class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dimension = 9
        rowsSet = [set() for _ in range(dimension)]
        colsSet = [set() for _ in range(dimension)]
        # colSet = Set() * dimension
        boxSet = [set() for row in range(dimension)]
        boxSet = defaultdict(set)

        for row in range(0, dimension):
            for column in range(0, dimension):
                if board[row][column] != ".":
                    if board[row][column] in rowsSet[row]:
                        return False
                    rowsSet[row].add(board[row][column])
                    if board[row][column] in colsSet[column]:
                        return False
                    colsSet[column].add(board[row][column])
                    # index = (row//3) * 3 + (column //3 )
                    if board[row][column] in boxSet[(row // 3, column // 3)]:
                        return False
                    boxSet[(row // 3, column // 3)].add(board[row][column])

        return True
