class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        totalWeight = sum(weights)
        daysNeeded, remainingWeight = 1, 0

        def canPackageBeShipped(currentShipCapacity):
            currentLoad,daysNeeded =0,1
            for index in range(len(weights)):
                currentLoad += weights[index]
                if currentLoad > currentShipCapacity:
                    currentLoad = weights[index]
                    daysNeeded += 1
            return daysNeeded <= days
        
        # perform binary search
        low,high  = max(weights),totalWeight
        
        while low <high:
            mid = low +(high-low)//2
            if canPackageBeShipped(mid):
                high = mid; 
            else:
                low = mid +1
        return low