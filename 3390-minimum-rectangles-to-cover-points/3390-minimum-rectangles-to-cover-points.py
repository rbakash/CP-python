class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        
        points.sort()
        minNoOfRectangles = 1
        i = 0
        firstPoint=points[0][0]

        for point in points:

            if point[0]> firstPoint+w:
                minNoOfRectangles += 1
                firstPoint = point[0]
        return minNoOfRectangles