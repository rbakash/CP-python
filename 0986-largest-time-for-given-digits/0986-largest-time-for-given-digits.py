class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        
        def isvalidTime(digits:str)-> bool:
            # first digit needs to be less than or equal to 2
            if int(digits[0])>2:
                return False
            if int(digits[0])==2 and int(digits[1])>3:
                return False
            if int(digits[2])>5:
                return False
            return True
            
        self.largestTime=""
        visited=set()
        
        def backTrack(currentTime:str, index):
            if index>3:
                return
            if len(currentTime) == 4:
                if isvalidTime(currentTime):
                    print(self.largestTime,currentTime)
                    self.largestTime = max(self.largestTime,currentTime)
                return
            
            for itx in range(4):
                if itx not in visited:
                    visited.add(itx)
                    backTrack(currentTime+str(arr[itx]),itx)
                    visited.remove(itx)
            return
        backTrack("",0)
        return "" if not self.largestTime else self.largestTime[:2]+":"+self.largestTime[2:]

