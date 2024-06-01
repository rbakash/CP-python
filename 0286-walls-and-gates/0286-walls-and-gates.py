class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows = len(rooms)
        cols = len(rooms[0])
        visited = set()
        queue = deque()
        direction = [[0, -1], [0, 1], [-1, 0], [1, 0]]

        for row in range(rows):
            for col in range(cols):
                if rooms[row][col] == 0:
                    queue.append((row, col))
                    visited.add((row, col))

        def addRooms(r,c):
            if r <0 or r == rows or c < 0 or c == cols or rooms[r][c] == -1 or (r, c) in visited:
                return
            queue.append((r, c))
            visited.add((r, c))

        distance = 0
        while queue:
            for idx in range(len(queue)):
                row, col = queue.popleft()
                rooms[row][col] = distance
                for r, c in direction:
                    r, c = row + r, col + c
                    addRooms(r, c)
            distance += 1

        return None
