class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = defaultdict(int)
        for task in tasks:
            freq[task] += 1
        maxHeap = [(-count, task) for task, count in freq.items()]
        heapify(maxHeap)
        time = 0
        while maxHeap:
            cycle = n + 1
            tempMaxHeap = []
            taskCount = 0
            while cycle>0 and maxHeap:
                currentCount, currentTask = heappop(maxHeap)
                if -currentCount > 1:
                    tempMaxHeap.append((currentCount + 1, currentTask))
                taskCount += 1
                cycle -= 1
            for tempCount, tempTask in tempMaxHeap:
                heappush(maxHeap,(tempCount, tempTask))
            time += taskCount if not maxHeap else n + 1
        return time
