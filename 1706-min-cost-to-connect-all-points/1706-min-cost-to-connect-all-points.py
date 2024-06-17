class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        parent = [num for num in range(n)]

        def find(node: int):

            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]

        def union(src: int, dest: int) -> bool:
            parentOfSrc = find(src)
            parentOfDest = find(dest)

            if parentOfSrc == parentOfDest:
                return False
            else:
                parent[parentOfDest] = parentOfSrc
            return True

        # Create weight for each src,dest
        allPoints = []
        for row in range(n):
            for nextRow in range(row + 1, n):
                weight = abs(points[row][0] - points[nextRow][0]) + abs(
                    points[row][1] - points[nextRow][1]
                )
                allPoints.append((weight, row, nextRow))

        # sort based on initial weight
        allPoints.sort()

        minCost = 0
        graph = []
        edgesUsed=0
        for weight, src, dest in allPoints:
            if union(src, dest):
                minCost += weight
                graph.append(src)
                graph.append(dest)
                edgesUsed+=1
            if edgesUsed == n - 1:
                break
        return minCost
