class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        color = [-1] * (n + 1)
        adj = defaultdict(list)

        # build the Adj matrix
        for node1, node2 in dislikes:
            adj[node1].append(node2)
            adj[node2].append(node1)

        def bfs(i):
            queue = deque()
            queue.append(i)
            color[i] = 0
            # color[0]= currentColor
            while queue:
                currentNode = queue.popleft()
                for eachNeighbor in adj[currentNode]:
                    if color[eachNeighbor] == color[currentNode]:
                        return False
                    if color[eachNeighbor] == -1:
                        color[eachNeighbor] = 1 - color[currentNode]
                        queue.append(eachNeighbor)
                        
            return True

        for index in range(1, n + 1):
            if color[index] == -1:
                if not bfs(index):
                    return False

        return True
