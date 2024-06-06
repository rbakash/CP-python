class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged=[]
        for eachInterval in intervals:
            if not merged or eachInterval[0] > merged[-1][1]:
                merged.append(eachInterval)
            else:
                merged[-1][1]=max(merged[-1][1],eachInterval[1])

        return merged