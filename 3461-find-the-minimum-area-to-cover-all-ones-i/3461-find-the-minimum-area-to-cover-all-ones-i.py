class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        # Start needs to be minimum
        widthStart,heightStart = float("inf"), float("inf")
        # End needs to be maximum to cover all the 1
        widthEnd, heightEnd  = float("-inf"), float("-inf")

        for currentRow in range(len(grid)):
            for currentColumn  in range(len(grid[0])):
                
                if grid[currentRow][currentColumn] ==1:
                    # Find the width start
                    widthStart = min(widthStart,currentColumn )

                    # Find the width End
                    widthEnd = max(widthEnd,currentColumn )

                    # Find the width start
                    heightStart = min(heightStart,currentRow )

                    # Find the width End
                    heightEnd = max(heightEnd,currentRow )
                    
        return ((widthEnd-widthStart)+1) *((heightEnd - heightStart)+1)
        