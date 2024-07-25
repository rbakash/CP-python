class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        undirectedAdjList=defaultdict(list)
        directedAdjList=set()
        visited=set()
        self.edgesChanged =0

        for src,dest in connections:
            undirectedAdjList[src].append(dest)
            undirectedAdjList[dest].append(src)
            directedAdjList.add((src,dest))
        
        
        def dfs(currentNode):
            if currentNode in visited:
                return
            visited.add(currentNode)
            for neighbor in undirectedAdjList[currentNode]:
                
                if neighbor not in visited:
                    if (currentNode,neighbor) in directedAdjList:
                        self.edgesChanged+=1
                    dfs(neighbor)
        dfs(0)
        return self.edgesChanged
        