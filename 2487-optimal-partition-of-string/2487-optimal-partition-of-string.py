class Solution:
    def partitionString(self, s: str) -> int:
        uniqueCharacter=set()
        numberOfPartition =1

        for character in s:
            if character in uniqueCharacter:
                numberOfPartition+=1
                uniqueCharacter.clear()
            
            uniqueCharacter.add(character)
        
        return numberOfPartition
            

        