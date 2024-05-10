class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-num for num in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:

            heaviestStone1 = heapq.heappop(maxHeap)
            heaviestStone2 = heapq.heappop(maxHeap)

            if heaviestStone1 != heaviestStone2:
                heapq.heappush(maxHeap, (heaviestStone1 - heaviestStone2))

        return -1 * maxHeap[0] if maxHeap else 0
