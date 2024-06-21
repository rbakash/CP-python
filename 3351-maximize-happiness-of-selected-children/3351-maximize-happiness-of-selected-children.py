class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        maxheap = [-num for num in happiness]
        heapify(maxheap)
        timeElapsed =0
        maxHappiness = 0

        while k > 0:
            maxElement = heappop(maxheap)*-1
            if maxElement - timeElapsed > 0:
                maxHappiness += (maxElement-timeElapsed)
            k-=1
            timeElapsed+=1
        
        return maxHappiness