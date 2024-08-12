class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratio=defaultdict(int)
        noOfPairs=0
        for currentWidth,currentHeight in rectangles:
            if currentWidth/currentHeight in ratio:
                noOfPairs+=ratio[currentWidth/currentHeight]
            ratio[currentWidth/currentHeight]+=1
        return noOfPairs