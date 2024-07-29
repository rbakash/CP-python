class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def getNextStates(currentCombination)->list:
            nextStates=[]
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
                    nextStates.append(newCombination)
            return nextStates
                
        
        if "0000" in deadends:
            return -1
        
        queue=deque([("0000")])
        moves=0
        visited = set()
        while queue:
            currentLevel = len(queue)
            for index in range(currentLevel):
                currentCombination = queue.popleft()
                if currentCombination == target:
                    return moves
                for eachStates in getNextStates(currentCombination):
                    if eachStates not in visited and eachStates not in deadends:
                            queue.append((eachStates))
                            visited.add(eachStates)
            moves+=1
        return -1

                        
