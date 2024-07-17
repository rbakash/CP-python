class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        adjList = defaultdict(list)
        noOfNodes=len(original)

        # build the adjacency list
        for index in range(noOfNodes):
            adjList[original[index]].append((changed[index],cost[index]))

        minimumDistances = {}
        
        def djisktras(source,destination):

            if (source,destination) in minimumDistances:
                return minimumDistances[(source,destination)]
            queue = []
            heappush(queue,(0,source))
            dist=[float("inf")]* 26
            dist[ord(source) - ord('a')] = 0

            while queue:
                currentCost,currentNode = heappop(queue)
                if currentNode == destination:
                    minimumDistances[(source, destination)] = currentCost
                    return currentCost
                if currentCost > dist[ord(currentNode)-ord('a')]:
                    continue

                for neighborNode,negihborCost in adjList[currentNode]:
                    
                    newCost = currentCost + negihborCost
                    if newCost < dist[ord(neighborNode)-ord('a')]:
                        dist[ord(neighborNode)-ord('a')] = newCost
                        heappush(queue,(newCost, neighborNode))

            return float('inf')

        # for every changed character, find the minimum cost 
        minimumCost =0
        for index in range(len(source)):
            # print(index)
            if source[index]!= target[index]:
                currentCost = djisktras(source[index],target[index])
                if currentCost == float("inf"):
                    return -1
                minimumCost += currentCost
        return minimumCost