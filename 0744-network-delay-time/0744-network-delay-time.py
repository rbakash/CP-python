class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adjList = defaultdict(list)
        # build adj list
        for src, dest, weight in times:
            adjList[src].append([dest, weight])

      

        minHeap = [[0, k]]
        ans = 0
        visited = set()

        while minHeap:
            currentWeight, currentNode = heappop(minHeap)
            if currentNode in visited:
                continue
            ans = max(ans, currentWeight)
            visited.add(currentNode)
            for neighborNode, neighborWeight in adjList[currentNode]:
                if neighborNode not in visited:
                    heappush(minHeap, [neighborWeight + currentWeight, neighborNode])
        if len(visited) == n:
            return ans 
        else:
            return -1
