class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adjList=defaultdict(list)
        for src in range(n-1):
            adjList[src].append(src+1)
        
        def bfs():
            queue=deque([0])
            distance=defaultdict(int)
            distance[0]=0
            visited = set([0])
            while queue:
                currentNode = queue.popleft()
                if currentNode == n-1:
                    return distance[currentNode]
                
                for eachNeighbor in adjList[currentNode]:
                    if eachNeighbor not in visited:
                        distance[eachNeighbor]= distance[currentNode]+1
                        visited.add(eachNeighbor)
                        queue.append(eachNeighbor)
            
            return float("inf")
        
        # find the shortestpath for first time
        answer=[]

        for src,dest in queries:
            # print(adjList)
            adjList[src].append(dest)
            shortest = bfs()
            answer.append(shortest)        
        return answer
