class Solution:
    def findWinningPlayer(self, A: List[int], k: int) -> int:
        # n = len(skills)
        # if n ==2:
        #     return 1 if skills[1]>skills[0] else 0

        # queue=[index for index in range(n)]
        # currentWinner = queue.pop(0)
        # consecutiveWins=0
        # maxSkill = 0
    
        # for idx in range(n):
        #     nextPlayer= queue.pop(0)
        #     if skills[nextPlayer]> skills[currentWinner]:
        #         consecutiveWins =1
        #         queue.append(currentWinner)
        #         currentWinner = nextPlayer
        #     else:
        #         consecutiveWins +=1
        #         queue.append(nextPlayer)

        #     if skills[idx] > skills[maxSkill]:
        #         maxSkill = idx
        #     if consecutiveWins == k or consecutiveWins >= n - 1:
        #         return currentWinner
        
        # return  maxSkill
        b = A[0]
        cur = -1
        for a in A:
            cur = 1 if a > b else cur + 1
            b = max(a, b)
            if cur == k:
                break
        return A.index(b)
        