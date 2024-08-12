class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        countGap=defaultdict(int)
        maxBrickEnds =0
        for index in range(len(wall)):
            position =0
            for currentBrick in wall[index][:-1]:
                countGap[position+currentBrick]+=1
                maxBrickEnds = max(maxBrickEnds,countGap[position+currentBrick])
                position+=currentBrick
        return len(wall) - maxBrickEnds
