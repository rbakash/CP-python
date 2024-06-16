class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result=[]

        def dfs(substring, path):
            if not substring:
                result.append(path)
                return

            for index in range(1,len(substring)+1):
                newPotentialString = substring[:index]
                if  newPotentialString == newPotentialString[::-1]:
                    dfs(substring[index:],path+[substring[:index]])
        dfs(s,[])
        return result
