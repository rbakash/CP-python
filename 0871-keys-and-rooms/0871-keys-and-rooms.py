class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visitedRooms = set()
        def dfs(currentKey):
            if currentKey in visitedRooms:
                return 

            visitedRooms.add(currentKey)
            for eachRoom in rooms[currentKey]:
                dfs(eachRoom)
        dfs(0)
        return len(visitedRooms) == len(rooms)