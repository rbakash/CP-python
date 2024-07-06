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
        queue.append((0, 0,0))
        visited = set()
        steps = 0
        while queue:
           # currentLevel = 1
            #for eachLevel in range(currentLevel):
            currentX, currentY,steps = queue.popleft()
            if (x,y) == (currentX,currentY):
                return steps
            for nextX, nextY in movements:
                newX, newY = (currentX + nextX), (currentY + nextY)
                if (newX, newY) not in visited:
                    queue.append((newX, newY,steps+1))
                    visited.add((newX, newY))
            
        return 0
