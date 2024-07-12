class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = defaultdict(list)
        for node1, node2, weight in edges:
            adj[node1].append((weight, node2))
            adj[node2].append((weight, node1))

        smallestNo = float('inf')
        smallestCity = -1

        for start in range(n):
            minHeap = [(0, start)]
            distances = {start: 0}
            while minHeap:
                currentWeight, currentNode = heappop(minHeap)
                if currentWeight > distanceThreshold:
                    continue
                for neighborWeight, neighborNode in adj[currentNode]:
                    newWeight = currentWeight + neighborWeight
                    if newWeight <= distanceThreshold and (neighborNode not in distances or newWeight < distances[neighborNode]):
                        distances[neighborNode] = newWeight
                        heappush(minHeap, (newWeight, neighborNode))
            
            reachableCities = len(distances) - 1  # Exclude the start city itself
            if reachableCities < smallestNo or (reachableCities == smallestNo and start > smallestCity):
                smallestNo = reachableCities
                smallestCity = start

        return smallestCity
