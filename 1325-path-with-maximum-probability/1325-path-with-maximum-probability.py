class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        for index,(node1,node2) in enumerate(edges):
            adj[node1].append((succProb[index],node2)) # node1: [(probab,node2)]
            adj[node2].append((succProb[index],node1))

        maxHeap = [(-1.0, start_node)]
        # heappush(maxHeap, )
        maxProbab=[0.0]*n
        maxProbab[start_node]=1.0
        
        while maxHeap:
            currentProbability, currentNode = heappop(maxHeap)
            currentProbability*=-1
            if currentNode == end_node:
                return currentProbability

            # for each negihbors, pick the one with largest probability
            for neighborProbab, neighborNode in adj[currentNode]:
                if neighborProbab * currentProbability > maxProbab[neighborNode]:
                    maxProbab[neighborNode] = neighborProbab * currentProbability
                    heappush(maxHeap, (-maxProbab[neighborNode],neighborNode ))
        return 0.0
