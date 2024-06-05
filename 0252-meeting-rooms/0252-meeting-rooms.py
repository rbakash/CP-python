class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        print(intervals)

        for index in range(1, len(intervals)):
            print(intervals[index-1][1],intervals[index][0])
            if intervals[index-1][1]-intervals[index][0]>0:
                return False
        return True