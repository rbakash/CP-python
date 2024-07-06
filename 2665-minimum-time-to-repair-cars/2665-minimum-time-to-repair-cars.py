class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def calculateNCars(time: int) -> bool:
            totalCars = 0
            for rank in ranks:
                totalCars += math.floor((time // rank) ** 0.5)
                if totalCars >= cars:
                    return False
            return True

        # binary search
        low, high = 1, max(ranks) * (cars) ** 2
        answer = -1
        while low <= high:
            mid = low + (high - low) // 2
            if calculateNCars(mid):
                low = mid + 1
            else:
                answer=mid
                high = mid - 1
        return answer
