class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        undirectedAdjList=defaultdict(list)
        directedAdjList=defaultdict(set)
        visited=set()
        self.edgesChanged =0

        for src,dest in connections:
            undirectedAdjList[src].append(dest)
            undirectedAdjList[dest].append(src)
            directedAdjList[src].add(dest)
        
        
        def dfs(currentNode):
            if currentNode == None:
                return
            visited.add(currentNode)
            for neighbor in undirectedAdjList[currentNode]:
                
                if neighbor not in visited:
                    if neighbor in directedAdjList[currentNode]:
                        self.edgesChanged+=1
                    dfs(neighbor)
        dfs(0)
        return self.edgesChanged
        