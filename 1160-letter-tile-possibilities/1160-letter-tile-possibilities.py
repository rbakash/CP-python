class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        ans = set()
        n = len(tiles)

        def dfs(currentTiles,currentString,size):
            if len(currentString) == size:
                ans.add(currentString)
                return
            
            for i in range(len(currentTiles)):
                dfs(currentTiles[:i]+currentTiles[i+1:],currentString + currentTiles[i], size )

        for size in range(1,n+1):
            dfs(tiles,"",size)

        return len(ans)
