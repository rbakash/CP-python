class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()

        for index in range(1, len(intervals)):
            if intervals[index-1][1]-intervals[index][0]>0:
                return False
        return True