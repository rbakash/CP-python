class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        answer = []
        characters = ["a", "b", "c"]

        if n ==1 and k > 3:
            return ""

        def backtrack(currentString: str):
            nonlocal k
            if len(currentString) == n:
                k-=1
                answer.append(currentString)
                return
            
            for eachCharacter in characters:
                if k == 0:
                    return
                if len(currentString) ==0  or eachCharacter != currentString[-1]:
                    
                    backtrack(currentString + eachCharacter)
            return 
        backtrack("")
        return answer[k - 1] if not k else ""
