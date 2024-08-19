class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # base condition
        # if no * and len is less, then pattern won't match
        if "*" not in p and len(p)!=len(s): 
            return False

        # remove the extra * to help reduce the recursion tree
        result=[]
        for char in p:
            if not result or char!="*":
                result.append(char)
            else:
                if result[-1]!="*":
                    result.append(char)
        p = "".join(result)
        print(p)
        dp={}
        def recursive(stringIndex,patternIndex):
            if (stringIndex,patternIndex) in dp:
                return dp[(stringIndex,patternIndex)]
            if stringIndex == len(s) and len(p) == patternIndex:
                return True

            if len(p) == patternIndex:
                dp[(stringIndex,patternIndex)] = False
                return False
            
            if len(s) == stringIndex and p[patternIndex] != "*":
                dp[(stringIndex,patternIndex)] = False
                return False
            
            # Else recur with next character
            if p[patternIndex] != "*":
                if p[patternIndex] =="?":
                    dp[(stringIndex,patternIndex)]  = recursive(stringIndex+1,patternIndex+1)
                    return dp[(stringIndex,patternIndex)]
                else:
                    dp[(stringIndex,patternIndex)]  = s[stringIndex] == p[patternIndex] and recursive(stringIndex+1,patternIndex+1)
                    return dp[(stringIndex,patternIndex)]
            else:
                # if its *, move the index to len(s)-remaing pattern
                nomatch = recursive(stringIndex, patternIndex+1)
                # Match 1 char.
                matchone = stringIndex <= len(s)-1 and recursive(stringIndex+1, patternIndex)
                dp[(stringIndex,patternIndex)] = nomatch or matchone
                return dp[(stringIndex,patternIndex)]
        return recursive(0,0)

                    