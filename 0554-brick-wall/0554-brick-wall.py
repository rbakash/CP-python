class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        endMap=defaultdict(int)
        maxBrickEnds =0
        for index in range(len(wall)):
            start =0
            for brick in wall[index][:-1]:
                endMap[start+brick]+=1
                maxBrickEnds = max(maxBrickEnds,endMap[start+brick])
                start+=brick

        return len(wall) - maxBrickEnds
