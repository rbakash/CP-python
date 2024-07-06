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
        x=abs(x)
        y=abs(y)
        while queue:

            currentX, currentY,steps = queue.popleft()
            if (x,y) == (currentX,currentY):
                return steps
            for nextX, nextY in movements:
                newX, newY = (currentX + nextX), (currentY + nextY)
                if (newX, newY) not in visited and -2 <= newX <= x + 2 and -2 <= newY <= y + 2:
                    queue.append((newX, newY,steps+1))
                    visited.add((newX, newY))
            
        return 0
