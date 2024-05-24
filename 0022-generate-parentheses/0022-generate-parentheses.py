class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        currentParanthesis = []
        allParanthesis = []

        def genrateAll(open, close):
            if open == close == n:
                allParanthesis.append("".join(currentParanthesis))
                return

            if open < n:
                currentParanthesis.append("(")
                genrateAll(open + 1, close)
                currentParanthesis.pop()

            if close < open:
                currentParanthesis.append(")")
                genrateAll(open, close + 1)
                currentParanthesis.pop()

        genrateAll(0, 0)
        return allParanthesis
