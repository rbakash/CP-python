class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize :
            return False

        frequency = {}
        for eachHand in hand:
            frequency[eachHand]=1+frequency.get(eachHand,0)

        minHeap = list(frequency.keys())
        heapq.heapify(minHeap)

        while minHeap:
            minElement = minHeap[0]
            for index in range(minElement, minElement+groupSize):
                if index not in frequency:
                    return False
                frequency[index]-=1
                if frequency[index] == 0:
                    if index != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        return True
                    


