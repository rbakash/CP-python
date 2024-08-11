class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        limit = 2000 + a+ b
        queue = deque([(0,True)])
        minHops=0
        visited=set(forbidden)

        while queue:
            level = len(queue)
            while level>0:
                level-=1
                currentElement, isForward = queue.popleft()
                if currentElement == x:
                    return minHops
                if currentElement in visited:
                    continue
                visited.add(currentElement)
                if isForward:
                    nextPosition = currentElement - b
                    if nextPosition >=0:
                        queue.append((nextPosition, False))
                nextPosition = currentElement + a
                if nextPosition <= limit:
                    queue.append((nextPosition,True))
            minHops+=1
        return -1
           
                
            
        