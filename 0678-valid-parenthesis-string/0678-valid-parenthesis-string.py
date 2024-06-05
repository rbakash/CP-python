class Solution:
    def checkValidString(self, s: str) -> bool:
        minCurrentOpenBrackets, maxCurrentOpenBrackets = 0, 0

        for character in s:
            
            if character == "(":
                minCurrentOpenBrackets, maxCurrentOpenBrackets = minCurrentOpenBrackets + 1,maxCurrentOpenBrackets + 1
            elif character == ")":
                    minCurrentOpenBrackets, maxCurrentOpenBrackets = minCurrentOpenBrackets - 1,maxCurrentOpenBrackets - 1
            else:
                # if its *, then we have two possibilities : ( or ), hence +1 and -1
                minCurrentOpenBrackets, maxCurrentOpenBrackets = minCurrentOpenBrackets - 1,maxCurrentOpenBrackets + 1
            
            # If max current is less than 0
            if maxCurrentOpenBrackets < 0:
                return False

            if minCurrentOpenBrackets < 0:
                minCurrentOpenBrackets = 0

        return minCurrentOpenBrackets == 0
