class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()
        parent = list(range(n))
        component = n
        rank = [0] * n

        def find(node1):
            if node1 != parent[node1]:
                parent[node1] = find(parent[node1])
            return parent[node1]

        def union(node1, node2):
            nonlocal component
            parent1 = find(node1)
            parent2 = find(node2)
            if parent1 == parent2:
                return True
            elif rank[parent1] > rank[parent2]:
                parent[parent2] = parent1
                rank[parent1] += 1
            elif rank[parent2] < rank[parent1]:
                parent[parent1] = parent2
                rank[parent2] += 1
            else:
                parent[parent2] = parent1
                rank[parent1] += 1
            component -= 1
            return False

        for timestamp, x, y in logs:
            union(x, y)
            if component == 1:
                return timestamp

        return -1
