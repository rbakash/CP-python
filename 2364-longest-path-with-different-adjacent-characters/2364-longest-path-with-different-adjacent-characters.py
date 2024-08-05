class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        self.maxLength = 1
        maxString=""
        adjList =defaultdict(list)
        for index in range(len(parent)):
            adjList[parent[index]].append(index)

        def dfs(root):
            if not adjList[root]:
                return 1
            lengthOfRoot = 1
            for eachNeigbhor in adjList[root]:
                childLength = dfs(eachNeigbhor)
                if s[root] != s[eachNeigbhor]:
                    self.maxLength = max(lengthOfRoot+childLength, self.maxLength)
                    lengthOfRoot = max(lengthOfRoot, childLength+1)
            return lengthOfRoot
        dfs(0)
        return self.maxLength
