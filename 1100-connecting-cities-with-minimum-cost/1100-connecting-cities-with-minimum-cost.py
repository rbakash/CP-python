class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        """Krushkal algorithm -> greedily find the lowest and keep adding it if it doesnot form cycle"""
        parent = list(range(n + 1))
        rank = [0] * (n + 1)
        numberOfComponents = n

        def find(node1):
            if node1 != parent[node1]:
                parent[node1] = find(parent[node1])
            return parent[node1]

        def union(node1, node2):
            nonlocal numberOfComponents
            parent1 = find(node1)
            parent2 = find(node2)
            if parent1 == parent2:
                return False
            elif rank[parent1] > rank[parent2]:
                parent[parent2] = parent1
                rank[parent1] += 1
            elif rank[parent2] > rank[parent1]:
                parent[parent1] = parent2
                rank[parent2] += 1
            else:
                parent[parent2] = parent1
                rank[parent1] += 1
            numberOfComponents -= 1
            return True

        # Sort it based on the weight
        # connections.sort(key=lambda node: node[2])
        # minCost, noOfNodesConnected = 0, 0

        # for node1, node2, weight in connections:
        #     if find(node1) == find(node2):
        #         continue
        #     union(node1, node2)
        #     minCost += weight
        #     noOfNodesConnected += 1
        #     if numberOfComponents == 1:
        #         return minCost

        # return -1
        """Prim's Algorithm -> pick any random node and keep adding the lowest weight from the neighbor if its not added already"""
        adj=defaultdict(list)
        visited = set()
        minCost=0
        minHeap=[(0,1)] # [cost, node]

        # build adj list
        for node1,node2, weight in connections:
            adj[node1].append((weight,node2))
            adj[node2].append((weight,node1))

        while minHeap and len(visited)< n:
            currentCost, currentNode = heappop(minHeap)
            if currentNode in visited:
                continue
            visited.add(currentNode)
            minCost +=currentCost
            for neighborCost, neighborNode in adj[currentNode]:
                if neighborNode not in visited:
                    heappush(minHeap,(neighborCost,neighborNode))
        
        if len(visited) < n:
            return -1
        else:
            return minCost