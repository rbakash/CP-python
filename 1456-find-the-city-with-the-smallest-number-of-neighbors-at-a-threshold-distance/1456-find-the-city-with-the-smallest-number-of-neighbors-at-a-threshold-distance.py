class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        adj = defaultdict(list)
        for node1, node2, weight in edges:
            adj[node1].append((weight, node2))
            adj[node2].append((weight, node1))
        smallestNo = float("inf")
        smallestCity = -1

        for node in range(n):
           
            cities = defaultdict(list)
            cities[node] = 0
            

            minHeap = [(0, node)]

            while minHeap:
                currentWeight, currentNode = heappop(minHeap)
                print(currentWeight, currentNode)
                if currentWeight > distanceThreshold:
                    continue

                # get all the negoihbor which satisfy the threshold
                for neighborWeight, neighborNode in adj[currentNode]:
                    newWeight = currentWeight + neighborWeight
                    if newWeight <= distanceThreshold and (neighborNode not in cities or newWeight < cities[neighborNode]):
                        cities[neighborNode] = newWeight
                        heappush(minHeap, (newWeight, neighborNode))
            reachableCity = len(cities) - 1
            if reachableCity < smallestNo or (reachableCity == smallestNo and node > smallestCity):
                smallestNo = reachableCity
                smallestCity = node
        return smallestCity
