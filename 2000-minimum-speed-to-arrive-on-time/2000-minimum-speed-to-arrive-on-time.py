class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        def timeTaken(speed: int) -> bool:
            timeNeeded = 0.0
            for index, eachDist in enumerate(dist):
                if index != n-1:
                    timeNeeded += math.ceil(eachDist / speed)
                else:
                    timeNeeded += eachDist / speed
                # print(timeNeeded)
                if timeNeeded > hour:
                    return False
            return True

        # Binary search
        low, high = 1, 10**7
        answer = -1
        while low <= high:
            mid = low + (high - low) // 2
            if timeTaken(mid):
                answer = mid
                high = mid - 1
            else:
                low = mid + 1
        return answer
