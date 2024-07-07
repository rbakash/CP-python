class Solution:
    def minMoves(self, rooks: List[List[int]]) -> int:
        sortedRows = sorted(rooks, key=lambda x: x[0])
        sortedCols = sorted(rooks, key=lambda x: x[1])
        moves, row = 0, 0
        for index in range(len(rooks)):
            moves += abs(sortedRows[index][0] - row) 
            moves += abs(sortedCols[index][1] - row)
            row += 1
        
        return moves
