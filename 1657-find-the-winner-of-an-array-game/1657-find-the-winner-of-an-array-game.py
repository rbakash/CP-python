class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        highestRatedPlayer = max(arr)
        if k>= highestRatedPlayer:
            return highestRatedPlayer

        queue=deque(arr)
        currentWinner = queue.popleft()
        winStreak =0

        while queue:
            opponent = queue.popleft()
            if opponent > currentWinner:
                queue.append(currentWinner)
                currentWinner = opponent
                winStreak =1
            else:
                queue.append(opponent)
                winStreak+=1
            if winStreak == k :
                return currentWinner
        return 1
        