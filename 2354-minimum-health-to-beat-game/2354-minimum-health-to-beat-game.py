class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        minDamage = sum(damage)
        minDamage -= armor if max(damage) > armor else max(damage)
        return minDamage+1
        