class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = max(piles)
        low, high = 1, maxPile

        while low < high:
            mid = low + (high - low) // 2

            # now check if the mid element is the minimum time needed
            hoursSpent = 0
            for pile in piles:
                hoursSpent += math.ceil(pile / mid)

            if hoursSpent <= h:
                high = mid
            else:
                low = mid + 1
        return low
