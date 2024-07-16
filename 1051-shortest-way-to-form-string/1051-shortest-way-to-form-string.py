class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        targetLength = len(target)
        sourceLength = len(source)
        sp,tp = 0,0 # tp-> target pointer, sp -> source pointer 
        minSubquence = 0
        sourceCharacter = set(source)

        # If we have any new character in target
        for targetCharacter in set(target):
            if targetCharacter not in sourceCharacter:
                return -1
        
        while tp < targetLength:

            # Cover as many target character from the source subsequence
            while sp<sourceLength and tp < targetLength :
                if source[sp] == target[tp]:
                    sp+=1
                    tp+=1
                else:
                    sp+=1
            
            # keep track of subsequence used
            minSubquence +=1
            # start from the begining for the next set of characters
            sp =0 

        return minSubquence