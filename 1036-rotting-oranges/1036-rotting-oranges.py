class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        visited = set()
        freshOranges = set()
        noOfMinute = 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2 and (row, col) not in visited:
                    queue.append((row, col))
                    visited.add((row, col))
                if grid[row][col] == 1:
                    freshOranges.add((row, col))

        if len(freshOranges) == 0:
            return 0

        def markRotten(row, col):
            if (
                row < 0
                or row == rows
                or col < 0
                or col == cols
                or (row, col) in visited
                or grid[row][col] == 0
            ):
                return
            queue.append((row, col))
            visited.add((row, col))

        while queue:
            for idx in range(len(queue)):
                currentRow, currentCol = queue.popleft()
                grid[currentRow][currentCol] = 2
                if (currentRow, currentCol) in freshOranges:
                    freshOranges.remove((currentRow, currentCol))
                for dr, dc in directions:
                    dr, dc = currentRow + dr, currentCol + dc
                    markRotten(dr, dc)
            noOfMinute += 1

        if len(freshOranges):
            return -1
        return noOfMinute-1
