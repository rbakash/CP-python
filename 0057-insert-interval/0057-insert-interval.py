class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged=[]
        intervals.append(newInterval)
        intervals.sort()

        for eachInterval in intervals:
           
            if not merged or  eachInterval[0] > merged[-1][1]:
                   merged.append(eachInterval)
            else:
            
                # overlapping intervals, merge them
                merged[-1][1]=max(merged[-1][1],eachInterval[1])
        
        return merged
        