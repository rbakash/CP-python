class Solution:
    def numOfMinutes(
        self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        queue = deque([(headID,0)])
        maxTime = 0
        adj=defaultdict(list)
        # Build adjacency
        for index in range(len(manager)):
            if manager[index]!=-1:
                adj[manager[index]].append(index)

        while queue:

            currentManager,time = queue.popleft()
            maxTime = max(maxTime, time)

            # find all the subordinates for current Manager
            for subOrdinates in adj[currentManager]:
                
                queue.append([subOrdinates,time+informTime[currentManager]])
           

        return maxTime
