class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # base condition
        # if no * and len is less, then pattern won't match
        if "*" not in p and len(p)!=len(s): 
            return False
        @lru_cache(maxsize = None)
        def recursive(stringIndex,patternIndex):
            if stringIndex == len(s) and len(p) == patternIndex:
                return True

            if len(p) == patternIndex:
                return False
            
            if len(s) == stringIndex and p[patternIndex] != "*":
                return False
            
            # Else recur with next character
            if p[patternIndex] != "*":
                if p[patternIndex] =="?":
                    return recursive(stringIndex+1,patternIndex+1)
                else:
                    return s[stringIndex] == p[patternIndex] and recursive(stringIndex+1,patternIndex+1)
            else:
                # if its *, move the index to len(s)-remaing pattern
                nomatch = recursive(stringIndex, patternIndex+1)
                # Match 1 char.
                matchone = stringIndex <= len(s)-1 and recursive(stringIndex+1, patternIndex)
                return nomatch or matchone
        return recursive(0,0)

                    