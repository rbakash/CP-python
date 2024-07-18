class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        indexesToDelete = set()

        for index in range(len(s)):
            
            if s[index] not in "()":
                continue
            elif s[index] == "(":
                stack.append(index)
            elif not stack:
                # invalid Close bracket, we need to remove it tp make it valid
                indexesToDelete.add(index)
            else:
                stack.pop()

        # add the remaining elements from stack
        while stack:
            indexesToDelete.add(stack.pop())
        
        result = ""
        for index in range(len(s)):
            if index not in indexesToDelete:
                result += s[index]
        
        return result
