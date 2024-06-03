class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n-1: return False
        parent = [num for num in range(n)]

        def find(x):
            while x != parent[x]:
                x = parent[x]
            return x

        def union(x, y):
            parentX = find(x)
            parentY = find(y)

            if parentX == parentY:
                return False
            else:
                parent[parentX] = parentY
                
                return True

        for src, dest in edges:
            if not union(src, dest):
                return False

        return True
