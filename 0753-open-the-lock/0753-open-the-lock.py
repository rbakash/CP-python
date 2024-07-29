class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        if "0000" in deadends:
            return -1
        
        def getNextStates(currentCombination)->list:
            nextStates=[]
            # every wheel combination
            for wheelIndex in range(4):
                # Each of the wheel can have 2 combination
                # Ex: 0000-> 1000 and 9000
                # postive rotation -> 0 to 1 or 1 to 2 etc
                newWheel = 0 if currentCombination[wheelIndex] == '9' else int(currentCombination[wheelIndex])+1
                newCombination = currentCombination[:wheelIndex]+str(newWheel) + currentCombination[wheelIndex+1:]
                nextStates.append(newCombination)

                # negative rotation -> 1 to 0 or 0 to 9 etc
                newWheel = 9 if currentCombination[wheelIndex] == '0' else int(currentCombination[wheelIndex])-1
                newCombination = currentCombination[:wheelIndex]+str(newWheel) + currentCombination[wheelIndex+1:]
                nextStates.append(newCombination)
            return nextStates
        
        queue=deque([("0000")])
        moves=0
        visited = set(deadends)
        while queue:
            currentLevel = len(queue)
            for index in range(currentLevel):
                currentCombination = queue.popleft()
                if currentCombination == target:
                    return moves
                for eachStates in getNextStates(currentCombination):
                    # print(eachStates)
                    if eachStates not in visited:
                            queue.append((eachStates))
                            visited.add(eachStates)
            moves+=1
        return -1

                        
