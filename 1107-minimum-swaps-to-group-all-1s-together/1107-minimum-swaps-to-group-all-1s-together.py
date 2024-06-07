class Solution:
    def minSwaps(self, data: List[int]) -> int:
        oneCount=0
        zeroCount =0
        minSwaps =999999

        # find all the occurences of 1
        for eachData in data:
            if eachData:
                oneCount+=1
        
        if oneCount ==1:
            return 0

        # windowSize = len(data)-oneCount
        for index in range(0,len(data)-oneCount+1):
            
            # check the 0's in the current window
            if zeroCount ==0:
                for zeroIndex in range(index,index+oneCount):
                    if not data[zeroIndex]:
                        zeroCount+=1
            else:
                if data[index-1] ==0:
                    zeroCount-=1
                if data[index+oneCount-1]==0:
                    zeroCount+=1
                    
            # minimum swaps will be min of current zero count and prev swaps count
            minSwaps = min(minSwaps,zeroCount)

        return minSwaps
         
        