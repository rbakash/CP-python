class Solution:
    def minimumOperationsToMakeEqualBFS(self, x: int, y: int) -> int:
        if x<=y:
            return y-x
        queue = deque([(x,0)])
        visited = set()
        visited.add(x)
        while queue:
            currentNum,turn = queue.popleft()
            if currentNum == y:
                return turn

            newNum = currentNum
            if currentNum-1>=0 and (currentNum-1) not in visited:
                newNum = currentNum-1
                queue.append((newNum,turn+1))
                visited.add(newNum)
            
            if  (currentNum+1) not in visited:
                newNum = currentNum+1
                queue.append((newNum,turn+1))
                visited.add(newNum)
            
            if currentNum % 11 == 0 and currentNum//11 not in visited:
                newNum = currentNum // 11
                queue.append((newNum,turn+1))
                visited.add(newNum)
            
            if currentNum % 5 == 0 and currentNum//5 not in visited:
                newNum = currentNum // 5
                queue.append((newNum,turn+1))
                visited.add(newNum)
            
            queue.append((newNum,turn+1))
            visited.add(newNum)
        
        return -1
            
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        if x <= y:
            return y-x
        operations = abs(x-y)
        operations = min(operations,1+x%5+self.minimumOperationsToMakeEqual(x//5,y))
        operations = min(operations,1+(5-x%5)+self.minimumOperationsToMakeEqual(x//5+1,y))
        operations = min(operations,1+x%11+self.minimumOperationsToMakeEqual(x//11,y))
        operations = min(operations,1+(11-x%11)+self.minimumOperationsToMakeEqual(x//11+1,y))
        return operations


    