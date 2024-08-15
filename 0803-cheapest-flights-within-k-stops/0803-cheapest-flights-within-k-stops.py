class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # build ADj list
        adj = defaultdict(list)
        for source, dest, cost in flights:
            adj[source].append([dest, cost])

        stops=[float("inf")]*n
        minHeap=[(0,src,0)] # node,cost,stops

        while minHeap:
            currentCost,currentNode,currentStops = heappop(minHeap)

            if currentStops > k+1 or currentStops > stops[currentNode]:
                continue
            stops[currentNode] = currentStops
            
            if currentNode == dst:
                return currentCost

            for eachNeigh,neighCost in adj[currentNode]:
                newCost = currentCost + neighCost
                heappush(minHeap, (newCost,eachNeigh,currentStops+1))

        return  -1
        
