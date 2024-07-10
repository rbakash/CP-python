class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        parent = list(range(n+1))
        rank = [0] * (n+1)

        def find(node1):
            if node1 != parent[node1]:
                parent[node1] = find(parent[node1])
            return parent[node1]

        def union(node1, node2):
            parent1 = find(node1)
            parent2 = find(node2)
            if parent1 == parent2:
                return False
            elif rank[parent1] > rank[parent2]:
                parent[parent2] = parent1
                rank[parent1] +=1
            elif rank[parent2] > rank[parent1]:
                parent[parent1] = parent2
                rank[parent2] +=1
            else:
                parent[parent2] = parent1
                rank[parent1] += 1
            return True

        # Sort it based on the weight
        connections.sort(key=lambda node: node[2])
        minCost, noOfNodesConnected = 0, 0

        for node1, node2, weight in connections:
            if find(node1) == find(node2):
                continue
            union(node1, node2)
            minCost += weight
            noOfNodesConnected += 1
        
        if noOfNodesConnected == n-1 :
            return minCost
        else:
            return -1
