class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        allPaths = []
        destination = len(graph) - 1

        def dfs(path, currentNode):

            if currentNode == destination:
                allPaths.append(path)
                return
                
            for neighbor in graph[currentNode]:
                if neighbor == destination:
                    allPaths.append(path + [neighbor])
                    continue
                dfs(path + [neighbor], neighbor)

        dfs([0], 0)
        return allPaths
