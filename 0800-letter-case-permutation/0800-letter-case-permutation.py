class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        answer=[]
        s = list(s)

        def backtrack(index,current):
            if index == len(s):
                answer.append(''.join(current))
                return
        
            if s[index].isalpha():
                # Try lowercase
                current[index] = current[index].lower()
                backtrack(index + 1, current)
                
                # Try uppercase
                current[index] = current[index].upper()
                backtrack(index + 1, current)
            else:
                backtrack(index + 1, current)

        backtrack(0,s)
        return answer