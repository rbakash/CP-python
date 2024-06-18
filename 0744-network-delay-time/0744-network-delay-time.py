class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adjList = defaultdict(list)
        # build adj list
        for src, dest, weight in times:
            adjList[src].append([dest, weight])

        # queue=deque()

        # cost[k]=0
        # queue.append(k)
        # while queue:
        #     currentNode = queue.popleft()

        #     for neighborNode,neighborWeight in adjList[currentNode]:
        #         if cost[neighborNode] > cost[currentNode]+neighborWeight:
        #             cost[neighborNode] = cost[currentNode]+neighborWeight
        #             queue.append(neighborNode)

        # return max(cost) if max(cost) != float(inf) else -1

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
                    heappush(
                        minHeap, [neighborWeight + currentWeight, neighborNode]
                    )
        return ans if len(visited) == n else -1
