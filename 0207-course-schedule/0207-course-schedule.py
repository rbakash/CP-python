class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if not prerequisites:
            return True

        preAdjacency = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for nodeA, nodeB in prerequisites:
            preAdjacency[nodeB].append(nodeA)
            indegree[nodeA] += 1

        queue = deque()
        noOfNodeVisisted = 0

        # Iterate through the list to find 0 in degree node
        for idx in range(numCourses):
            if indegree[idx] == 0:
                queue.append(idx)

        # reduce the adj nodes of all zero indregree nodes
        while queue:
            currentNode = queue.popleft()
            noOfNodeVisisted += 1

            for eachNeighbhor in preAdjacency[currentNode]:
                indegree[eachNeighbhor] -= 1
                if indegree[eachNeighbhor] == 0:
                    queue.append(eachNeighbhor)
        return noOfNodeVisisted == numCourses

        # def dfs(nums):

        #     if nums in visited:
        #         return False
        #     if preAdjacency[nums] == []:
        #         return True
        #     visited.add(nums)
        #     for eachPreReq in preAdjacency[nums]:
        #         if not dfs(eachPreReq):
        #             return False
        #     visited.remove(nums)
        #     preAdjacency[eachPreReq] = []

        #     return True

        # # for num in range(numCourses):
        # #     if not dfs(num):
        # #         return False
        # # return True
