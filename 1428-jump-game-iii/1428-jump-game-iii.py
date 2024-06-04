class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)

        if start >= 0 and start < n and arr[start]>=0:

            if arr[start] == 0:
                return True
            arr[start] *= -1
            return self.canReach(arr,start + arr[start]) or self.canReach(arr,start - arr[start])
        return False
