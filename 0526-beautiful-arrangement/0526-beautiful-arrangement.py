class Solution:
    def countArrangement(self, n: int) -> int:
        visited =set()
        numbers = list(range(n+1))
        numberOfArrangements = 0
        def backTrack(currentArrangement, index,length)->int:
            nonlocal numberOfArrangements
            if len(currentArrangement) == n:
                numberOfArrangements+=1
                return numberOfArrangements

            for iterator in range(1,n+1):
                if numbers[iterator] not in visited and (((len(currentArrangement)+1) % numbers[index] == 0 ) or (numbers[index] % (len(currentArrangement) +1) == 0)):
                    currentArrangement.append(numbers[iterator])
                    visited.add(numbers[iterator])
                    backTrack(currentArrangement, iterator, len(currentArrangement))
                    # print(visited, currentArrangement)
                    currentArrangement.pop()
                    visited.remove(numbers[iterator])
            return numberOfArrangements
        backTrack([],1,0)
        return numberOfArrangements
        