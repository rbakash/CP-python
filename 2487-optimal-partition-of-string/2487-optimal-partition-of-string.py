class Solution:
    def partitionString(self, s: str) -> int:
        uniqueCharacter=set()
        numberOfPartition =0

        for character in s:
            if character in uniqueCharacter:
                numberOfPartition+=1
                uniqueCharacter.clear()
            
            uniqueCharacter.add(character)
        
        return numberOfPartition+1
            

        