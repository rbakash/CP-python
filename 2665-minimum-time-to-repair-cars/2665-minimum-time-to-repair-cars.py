class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def calculateNCars(time: int) -> bool:
            totalCars = 0
            for rank in ranks:
                totalCars += math.floor((time // rank) ** 0.5)
            return totalCars < cars

        # binary search
        low, high = 1, max(ranks) * (cars) ** 2
        while low <= high:
            mid = low + (high - low) // 2
            if calculateNCars(mid):
                low = mid + 1
            else:
                high = mid - 1
        return low
