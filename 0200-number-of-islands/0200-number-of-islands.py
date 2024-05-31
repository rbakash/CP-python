class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        noOfIslands = 0
        if not grid:
            return noOfIslands
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def dfs(currentRow, currentCol):
            if (
                currentRow < 0
                or currentRow == rows
                or currentCol < 0
                or currentCol == cols
                or grid[currentRow][currentCol] != "1"
            ):
                return
            grid[currentRow][currentCol] = "0"

            dfs(currentRow - 1, currentCol)
            dfs(currentRow + 1, currentCol)
            dfs(currentRow, currentCol - 1)
            dfs(currentRow, currentCol + 1)

        def bfs(row, col):
            queue = deque()
            queue.append((row, col))
            visited.add((row, col))

            while queue:
                currentRow, currentCol = queue.popleft()
                directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                for dr, dc in directions:
                    r, c = currentRow + dr, currentCol + dc
                    if (
                        r in range(rows)
                        and c in range(cols)
                        and grid[r][c] == "1"
                        and (r, c) not in visited
                    ):
                        visited.add((r, c))
                        queue.append((r, c))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    # dfs(row, col)
                    bfs(row, col)
                    noOfIslands += 1
        return noOfIslands
