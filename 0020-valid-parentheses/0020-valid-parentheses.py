class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) == 1:
            return False
        for bracket in s:
            if bracket == "(" or bracket == "{" or bracket == "[":
                stack.append(bracket)
            elif len(stack) == 0:
                return False
            else:
                latestBracket = stack.pop()
                if bracket == ")" and latestBracket != "(":
                    return False
                if bracket == "}" and latestBracket != "{":
                    return False
                if bracket == "]" and latestBracket != "[":
                    return False
        return len(stack) == 0
