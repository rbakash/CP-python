class Solution:
    def reorganizeString(self, s: str) -> str:
        freq={}
        for eachCharacter in s:
            freq[eachCharacter]=freq.get(eachCharacter,0)-1
        maxHeap=[(count,char) for char,count in freq.items()]
        heapq.heapify(maxHeap)
        prev=None
        result =[]
        
        while maxHeap:
            firstFreq, firstChar = heappop(maxHeap)
            if not result or firstChar != result[-1]:
                result.append(firstChar)
                if firstFreq+1 != 0 :
                    heappush(maxHeap, (firstFreq+1,firstChar))
                
            else:
                if not maxHeap: return ""
                secondMaxFreq, secondMostChar = heappop(maxHeap)
                result.append(secondMostChar)
                if secondMaxFreq +1 != 0 :
                    heappush(maxHeap, (secondMaxFreq+1,secondMostChar))
                heappush(maxHeap,(firstFreq,firstChar))
        return "".join(result)