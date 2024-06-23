class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        return (sum(damage) - (armor if max(damage) > armor else max(damage))) +1
        