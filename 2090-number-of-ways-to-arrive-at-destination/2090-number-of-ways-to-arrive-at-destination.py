class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adjList=defaultdict(list)
        distance= [float("inf")]*n

        # create  the graph
        for src,dest,weight in roads:
            adjList[src].append((dest,weight))
            adjList[dest].append((src,weight))

        minHeap = [(0,0)]
        noOfPaths=[0]*n
        noOfPaths[0]=1
        
        while minHeap:
            currentWeight,currentNode = heappop(minHeap)
            
            for eachNeigbhor, neigbhorWeight in adjList[currentNode]:
                newWeight= currentWeight + neigbhorWeight
                if newWeight < distance[eachNeigbhor] :
                    distance[eachNeigbhor]=newWeight
                    noOfPaths[eachNeigbhor]=noOfPaths[currentNode]
                    heappush(minHeap, (newWeight, eachNeigbhor))
                elif newWeight == distance[eachNeigbhor] :
                    noOfPaths[eachNeigbhor]=(noOfPaths[currentNode] + noOfPaths[eachNeigbhor]) % (10**9 + 7)
            
        # now just count the shortest pat
        return noOfPaths[n-1]

