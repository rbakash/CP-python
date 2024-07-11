class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        rows = len(grid)
        cols = len(grid[0])

        def bfs(currentScore: int) -> bool:
            queue = deque()
            visited = set()
            queue.append((0, 0))  # (row, col)
            

            while queue:
                currentRow, currentCol = queue.popleft()
                if currentRow == rows - 1 and currentCol == cols - 1:
                    return True
                for rowOffset, colOffSet in dirs:
                    newRow, newCol = currentRow + rowOffset, currentCol + colOffSet
                    
                    if not (0 <= newRow < rows and 0 <= newCol < cols):
                        continue
                    # print(newRow, newCol)
                    if grid[newRow][newCol] >= currentScore and (newRow, newCol) not in visited:
                        visited.add((newRow, newCol))
                        queue.append((newRow, newCol))
            return False

        low, high = 0, min(grid[0][0], grid[-1][-1])
        while low < high:
            mid = low + (high - low) // 2
            print(mid)
            if bfs(mid):
                low = mid+1
            else:
                high = mid - 1

        return low - 1 if not bfs(low) else low
