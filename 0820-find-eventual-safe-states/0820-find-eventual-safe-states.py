class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        outdegree = [0] * n
        adj = [[] for _ in range(n)]
        safeNodes = []

        # build the indegree of each node
        for currentNode, neigbhors in enumerate(graph):
            for eachNeighbor in neigbhors:
                adj[eachNeighbor].append(currentNode)
                outdegree[currentNode] += 1
        queue = deque()
        # extract out nodes with outdegree == 0
        for index in range(n):
            if outdegree[index] == 0:
                queue.append(index)
        safe=[False]*n
        while queue:
            currentNode = queue.popleft()
            # safeNodes.append(currentNode)
            safe[currentNode]=True
            for neighbor in adj[currentNode]:
                outdegree[neighbor] -= 1
                if outdegree[neighbor] == 0:
                    queue.append(neighbor)
        for index in range(n):
            if safe[index]:
                safeNodes.append(index)
        return safeNodes
