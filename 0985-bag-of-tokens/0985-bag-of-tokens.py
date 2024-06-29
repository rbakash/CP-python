class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        low, high,score=0,len(tokens)-1,0
        while low<= high:
            if tokens[low] <= power:
                score+=1
                power-=tokens[low]
                low+=1
            elif low< high and score > 0:
                power +=tokens[high]
                high-=1
                score-=1
            else:
                break
        return score