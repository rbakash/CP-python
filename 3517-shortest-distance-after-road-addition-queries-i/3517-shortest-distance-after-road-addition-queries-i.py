class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adjList=defaultdict(list)
        for src in range(n-1):
            adjList[src].append((src+1,1))
        
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
        
        def djisktra()->int:
            visited=set()
            distance=[float("inf")]*n
            distance[0]=0
            minHeap = [(0,0)]

            while minHeap:
                currentNode, currentDistance = heappop(minHeap)
                if currentNode == n-1:
                    return distance[n-1]
                if currentNode in visited or currentDistance > distance[currentNode]:
                    continue
                
                visited.add(currentNode)
                for eachNeighbor,weight in adjList[currentNode]:
                    if eachNeighbor in visited:
                        continue
                    newDistance = currentDistance+weight
                    if newDistance < distance[eachNeighbor]:
                        # Update the weight
                        distance[eachNeighbor]=newDistance
                        heappush(minHeap,(eachNeighbor,newDistance))
            return distance[n-1]
                
        # find the shortestpath for first time
        answer=[]

        for src,dest in queries:
            # print(adjList)
            adjList[src].append((dest,1))
            shortest = djisktra()
            answer.append(shortest)        
        return answer
