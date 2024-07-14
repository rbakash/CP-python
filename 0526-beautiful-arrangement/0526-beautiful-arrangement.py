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

                if number not in currentArrangement and (((len(currentArrangement)+1) % number == 0 ) or (number % (len(currentArrangement) +1) == 0)):
                    # Add the current combination
                    currentArrangement.append(number)
                   
                    backTrack(currentArrangement)

                    # Backtrack 
                    currentArrangement.pop()
            return numberOfArrangements
        
        return backTrack([])
        