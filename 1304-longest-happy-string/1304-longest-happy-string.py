class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap =[]
        for count,char in [(-a,"a"),(-b,"b"),(-c,"c")]:
            if count != 0:
                heapq.heappush(maxHeap,(count,char))

        answer=""

        while maxHeap:
            currentCount, currentCharacter = heappop(maxHeap)
            print(answer,maxHeap,currentCharacter)
            if len(answer)> 1 and answer[-1]==answer[-2]  == currentCharacter:
                if not maxHeap:
                    break
                nextCount, nextCharacter = heappop(maxHeap)
                answer+=nextCharacter
                heappush(maxHeap, (currentCount,currentCharacter))
                if nextCount !=-1:
                    heappush(maxHeap, (nextCount+1, nextCharacter))
            else:
                answer+=currentCharacter
                if currentCount !=-1:
                    heappush(maxHeap, (currentCount+1,currentCharacter))

        return answer