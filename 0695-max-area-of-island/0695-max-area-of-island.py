class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0
        visited = set()

        direction = [[0, -1], [0, 1], [-1, 0], [1, 0]]

        def bfs(currentRow, currentCol):

            queue = deque()

            queue.append((currentRow, currentCol))
            visited.add((currentRow, currentCol))
            currentArea = 1
            while queue:
                row, col = queue.pop()
                for dr, dc in direction:
                    r, c = row + dr, col + dc
                    if (
                        r in range(rows)
                        and c in range(cols)
                        and grid[r][c] == 1
                        and (r, c) not in visited
                    ):
                        queue.append((r, c))
                        visited.add((r, c))
                        currentArea += 1
            return currentArea

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:

                    currentArea = bfs(row, col)
                    maxArea = max(currentArea, maxArea)

        return maxArea
