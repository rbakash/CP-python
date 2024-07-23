class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq=defaultdict(int)
        for num in arr:
            freq[num]+=1
        
        minHeap=[(count,num) for num,count in freq.items()]
        heapify(minHeap)
        while k:
            count,currentNum=heappop(minHeap)
            if count > k:
               return len(freq)
            else:
                k-=count
                del freq[currentNum]
        return len(freq)
