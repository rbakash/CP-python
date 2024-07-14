class Solution:
    def countArrangement(self, n: int) -> int:
        visited =set()
        numberOfArrangements = 0

        def backTrack(currentArrangement)->int:
            nonlocal numberOfArrangements
            # Valid Arrangements
            if len(currentArrangement) == n:
                numberOfArrangements+=1
                return numberOfArrangements

            for number in range(1,n+1):
                length = len(currentArrangement)+1
                if number not in visited and (length % number == 0  or number % length == 0):
                    # Add the current combination
                    currentArrangement.append(number)
                    visited.add(number)

                    backTrack(currentArrangement)

                    # Backtrack 
                    currentArrangement.pop()
                    visited.remove(number)
            return numberOfArrangements
        
        return backTrack([])
        