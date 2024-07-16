class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap =[]
        if a > 0:
            heapq.heappush(maxHeap, (-a, 'a'))
        if b > 0:
            heapq.heappush(maxHeap, (-b, 'b'))
        if c > 0:
            heapq.heappush(maxHeap, (-c, 'c'))

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