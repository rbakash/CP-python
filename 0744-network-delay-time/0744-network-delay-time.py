class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        cost=[float('inf')]* (n+1)
        cost[0]=0

        adjList=[[] for eachNode in range(n+1)]
        # build adj list
        for src,dest,weight in times:
            adjList[src].append([dest,weight])

        queue=deque()

        cost[k]=0
        queue.append(k)
        while queue:
            currentNode = queue.popleft()
           
            for neighborNode,neighborWeight in adjList[currentNode]:
                if cost[neighborNode] > cost[currentNode]+neighborWeight:
                    cost[neighborNode] = cost[currentNode]+neighborWeight
                    queue.append(neighborNode)

        return max(cost) if max(cost) != float(inf) else -1