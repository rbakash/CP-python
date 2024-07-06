class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        movements = [
            (2, 1),
            (1, 2),
            (-1, 2),
            (-2, 1),
            (-2, -1),
            (-1, -2),
            (1, -2),
            (2, -1),
        ]
        queue = deque()
        queue.append((0, 0))
        visited = set()
        steps = 0
        while queue:
            currentLevel = len(queue)
            for eachLevel in range(currentLevel):
                currentX, currentY = queue.popleft()
                if (x,y) == (currentX,currentY):
                    return steps
                for nextX, nextY in movements:
                    newX, newY = (currentX + nextX), (currentY + nextY)
                    if (newX, newY) not in visited:
                        queue.append((newX, newY))
                        visited.add((newX, newY))
            steps += 1
        return steps
