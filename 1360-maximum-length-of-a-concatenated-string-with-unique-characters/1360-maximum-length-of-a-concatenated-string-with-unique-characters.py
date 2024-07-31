class Solution:
    def maxLength(self, arr: List[str]) -> int:
        validConcatenations =[]
        self.maxLength =0
        def isValidConcatenations(string:str)->bool:

            if len(set(string)) == len(string):
                return True
            else:
                return False

        def backtrack(currentString,index):
            if not isValidConcatenations(currentString):
                return
            else:
                self.maxLength=max(self.maxLength,len(currentString))
                validConcatenations.append(currentString)
            
            for itx in range(index,len(arr)):
                    backtrack(currentString+arr[itx],itx+1)

        backtrack("",0)
        return self.maxLength