class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
     # All 8 possible moves a knight can make
        directions = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]

        # Use absolute values for symmetry
        x, y = abs(x), abs(y)
        
        # BFS initialization
        queue = deque([(0, 0, 0)])  # (current_x, current_y, steps)
        visited = set((0, 0))
        
        while queue:
            cur_x, cur_y, steps = queue.popleft()
            
            # If we reach the target, return the number of steps
            if cur_x == x and cur_y == y:
                return steps
            
            # Try all possible moves
            for dx, dy in directions:
                new_x, new_y = cur_x + dx, cur_y + dy
                
                # Only add new position to queue if it hasn't been visited
                if (new_x, new_y) not in visited and -2 <= new_x <= x + 2 and -2 <= new_y <= y + 2:
                    visited.add((new_x, new_y))
                    queue.append((new_x, new_y, steps + 1))
