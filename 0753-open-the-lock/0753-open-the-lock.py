class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        queue=deque([("0000",0)])
        visited = set()
        while queue:
            currentLevel = len(queue)
            currentCombination,currentMove = queue.popleft()
           

            if currentCombination == target:
                return currentMove

                # every wheel combination
            for wheelIndex in range(4):
                # Each of the wheel can have 2 combination
                # Ex: 0000-> 1000 and 9000
                for delta in [-1,1]:
                    if currentCombination[wheelIndex] =='0' and delta==-1:
                        newWheel = 9
                    else:
                        newWheel = (int(currentCombination[wheelIndex])+ delta)%10
                    newCombination = currentCombination[:wheelIndex]+str(newWheel) + currentCombination[wheelIndex+1:]

                    if newCombination not in visited and newCombination not in deadends:
                        queue.append((newCombination,currentMove+1))
                        visited.add(newCombination)
        return -1

                        
