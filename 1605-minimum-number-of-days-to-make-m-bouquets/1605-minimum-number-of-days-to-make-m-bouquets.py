class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        def calculateBoquetforAGivenDay(day: int) -> int:
            noOfBoquet, count = 0, 0
            for eachBloom in bloomDay:
                if eachBloom <= day:
                    count += 1
                else:
                    count = 0
                if count == k:
                    noOfBoquet += 1
                    count = 0

            return noOfBoquet

        # Binary search
        low, high = min(bloomDay), max(bloomDay)
        minDays = -1
        while low <= high:
            mid = low + (high - low) // 2
            currentBoquets = calculateBoquetforAGivenDay(mid)
            if currentBoquets >= m:
                minDays = mid
                high = mid - 1
            else:
                low = mid + 1
        return minDays
