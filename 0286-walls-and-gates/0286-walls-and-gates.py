class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        # if not -1 or 0 we gotta calculate the distance.add(a, b)
        if not rooms or not rooms[0]:
            return
        rows = len(rooms)
        cols = len(rooms[0])
        visited = set()
        queue = collections.deque()
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r, c))
                    # visited.add((r, c))
        distance = 0
        while queue:

            for _ in range(len(queue)):
                row, col = queue.popleft()
               
                # we return if the node has been visited already with a shorter distance and if its a gate or wall
                if (
                    row < 0
                    or row == rows
                    or col < 0
                    or col == cols
                    or rooms[row][col] == -1
                    or (row, col) in visited
                ):
                    
                    continue;
                rooms[row][col] = distance
                visited.add((row, col))
                queue.append((row + 1, col))
                queue.append((row - 1, col))
                queue.append((row, col + 1))
                queue.append((row, col - 1))
                # print(queue)
            distance += 1
        return None
