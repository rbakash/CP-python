class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if not prerequisites:
            return True

        preAdjacency = {i: [] for i in range(numCourses)}
        visited = set()
        for nodeA, nodeB in prerequisites:
            preAdjacency[nodeA].append(nodeB)

        def dfs(nums):

            if nums in visited:
                return False
            if preAdjacency[nums] == []:
                return True
            visited.add(nums)
            for eachPreReq in preAdjacency[nums]:
                if not dfs(eachPreReq):
                    return False
            visited.remove(nums)
            preAdjacency[eachPreReq] = []

            return True

        for num in range(numCourses):
            if not dfs(num):
                return False
        return True
