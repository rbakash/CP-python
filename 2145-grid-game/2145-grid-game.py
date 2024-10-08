class Solution:
    def gridGame(self, g: List[List[int]]) -> int:
        top, bottom, res = sum(g[0]), 0, math.inf
        for g0, g1 in zip(g[0], g[1]):
            top -= g0
            res = min(res, max(top, bottom))
            bottom += g1
        return res
