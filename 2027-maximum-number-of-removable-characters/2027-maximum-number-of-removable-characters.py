class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        char = list(s)
        def isSubsequence(mid) -> bool:
            removedIndices = set(removable[:mid])
            # removedIndices = {removable[i] for i in range(mid)}
            p1,p2 =0,0
            while p1< len(s) and p2<len(p):
                if p1 not in removedIndices:
                    if s[p1] == p[p2]:
                        p2+=1
                p1+=1
            return p2 == len(p)

        low, high = 0, len(removable)
        minK = 0
        while low <= high:
            mid = low + (high - low) // 2
            if isSubsequence(mid):
                minK = mid
                low = mid + 1
                
            else:
                high = mid - 1
        return minK
