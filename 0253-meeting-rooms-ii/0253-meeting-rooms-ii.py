class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        minHeap = []
        heapq.heappush(minHeap, intervals[0][1])

        for interval in intervals[1:]:
            if interval[0] >= minHeap[0]:
                heapq.heappop(minHeap)

            heapq.heappush(minHeap, interval[1])
        return len(minHeap)
