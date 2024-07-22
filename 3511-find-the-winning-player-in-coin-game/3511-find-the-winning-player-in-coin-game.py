class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        minTurn = min(x, y//4)
        return "Bob" if minTurn %2 == 0 else "Alice" 