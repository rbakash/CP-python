class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [num for num in range(n)]

        def find(x):
            while x != parent[x]:
                x = parent[x]
            return x

        def union(x, y):
            parentX = find(x)
            parentY = find(y)
            if parentX != parentY:
                parent[parentX] = parentY

        for src, dest in edges:
            union(src, dest)

        disconnectedComponent = 0
        for idx in range(n):
            if idx == parent[idx]:
                disconnectedComponent+=1

        return disconnectedComponent
