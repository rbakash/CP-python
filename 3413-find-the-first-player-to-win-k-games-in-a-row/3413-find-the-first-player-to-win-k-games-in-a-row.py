class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        n = len(skills)
        if n ==2:
            return 1 if skills[1]>skills[0] else 0

        queue=[index for index in range(n)]
        currentWinner = queue.pop(0)
        consecutiveWins=0
        maxSkill = max(skills)
    
        for idx in range(n):
            nextPlayer= queue.pop(0)
            if skills[nextPlayer]> skills[currentWinner]:
                consecutiveWins =1
                queue.append(currentWinner)
                currentWinner = nextPlayer
            else:
                consecutiveWins +=1
                queue.append(nextPlayer)

            if consecutiveWins == k or skills[idx] == maxSkill:
                return currentWinner

        