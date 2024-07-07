class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        parent = [i for i in range(n)]
        rank = [0] * n
        component = n

        def find(nodeX):
            if nodeX == parent[nodeX]:
                return nodeX
            else:
                parent[nodeX] = find(parent[nodeX])
            return parent[nodeX]

        def union(nodeX, nodeY):
            parentX = find(nodeX)
            parentY = find(nodeY)

            if parentX != parentY:
                if rank[parentX] > rank[parentY]:
                    parent[parentY] = parentX
                elif rank[parentY] > rank[parentX]:
                    parent[parentX] = parentY
                else:
                    parent[parentY] = nodeX
                    rank[nodeX] += 1
                return 1
            return 0

        def isSameRowOrColumn(stone1, stone2):
            return stone1[0] == stone2[0] or stone1[1] == stone2[1]

        for row in range(n):
            for column in range(row + 1, n):
                if isSameRowOrColumn(stones[row], stones[column]):
                    component -= union(row, column)

        return n - component
