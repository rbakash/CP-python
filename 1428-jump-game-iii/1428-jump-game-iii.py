class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        queue = deque()
        queue.append(start)

        while queue:
            currentNode = queue.popleft()
            if arr[currentNode] == 0:
                return True
            if arr[currentNode]<0:
                continue
            if currentNode + arr[currentNode] < n :
                queue.append(currentNode +arr[currentNode])
            if  currentNode - arr[currentNode] >=0:
                queue.append(currentNode - arr[currentNode])
            arr[currentNode]*=-1
        return False
