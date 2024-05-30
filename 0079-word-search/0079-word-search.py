class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        wordLength = len(word)
        path = set()

        def dfs(currentRow, currentCol, stringIndex):
            if stringIndex == wordLength:
                return True

            if (
                currentRow < 0
                or currentRow >= rows
                or currentCol < 0
                or currentCol >= cols
                or board[currentRow][currentCol] != word[stringIndex]
                or (currentRow, currentCol) in path
            ):
                return False

            path.add((currentRow, currentCol))
            isValid = (
                dfs(currentRow - 1, currentCol, stringIndex + 1)
                or dfs(currentRow + 1, currentCol, stringIndex + 1)
                or dfs(currentRow, currentCol - 1, stringIndex + 1)
                or dfs(currentRow, currentCol + 1, stringIndex + 1)
            )
            path.remove((currentRow, currentCol))
            return isValid

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True
        return False
