class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        minHeap = []
        for index in range(len(heights) - 1):
            heightDifference = heights[index + 1] - heights[index]
            if heights[index + 1] > heights[index]:
                # need brick or ladder to go to next building
                if ladders > 0:
                    ladders -= 1
                    heappush(minHeap, (heightDifference))
                else:
                    if not minHeap or heightDifference < minHeap[0]:
                        # Need to swap the bricks and ladder to use the ladder for max height
                        bricks -= heightDifference
                    else:
                        smallestJump = heappop(minHeap)
                        heappush(minHeap, heightDifference)
                        bricks -= smallestJump
                    if bricks < 0:
                        return index
        return len(heights) - 1
