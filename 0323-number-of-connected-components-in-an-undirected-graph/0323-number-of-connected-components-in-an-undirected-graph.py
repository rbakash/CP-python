class Solution:
    def countComponents(self, count: int, edges: List[List[int]]) -> int:
        parent = [num for num in range(count)]

        def findParent(x):
            # find the root parent
            if x != parent[x]:
                parent[x] = findParent(parent[x])
            return parent[x]

        def union(x, y):
            parentx = findParent(x)
            parenty = findParent(y)
            if parentx != parenty:
                parent[parenty] = parentx
                return True
            else:
                return False

        for start, end in edges:
            if union(start, end):
                count -= 1
        return count
