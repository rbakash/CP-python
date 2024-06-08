class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        queue=deque(arr)
        currentWinner = queue.popleft()
        highestRatedPlayer = max(arr)
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
            if winStreak == k or currentWinner==highestRatedPlayer:
                return currentWinner
        return 1
        