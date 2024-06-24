class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        ans =1
        arr.sort()
        for index in range(1, len(arr)):
            if arr[index] >= ans+1: ans +=1
        return ans
