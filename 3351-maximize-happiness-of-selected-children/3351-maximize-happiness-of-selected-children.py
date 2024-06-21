class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # maxheap = [-num for num in happiness]
        # heapify(maxheap)
        happiness.sort(reverse=True)
        timeElapsed =0
        maxHappiness = 0

        while k > 0:
            maxElement = happiness[timeElapsed]
            if maxElement - timeElapsed > 0:
                maxHappiness += (maxElement-timeElapsed)
            k-=1
            timeElapsed+=1
        
        return maxHappiness