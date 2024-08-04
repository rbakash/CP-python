class HitCounter:

    def __init__(self):
        self.hits=[]
        self.low=0
        self.totalHits =0    

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)
        self.totalHits+=1
        

    def getHits(self, timestamp: int) -> int:
        # perfomr binary search till timestamp -300
        target = timestamp-300
        high =self.totalHits-1
        
        while self.low<=high:
            mid = (self.low+high)//2
              
            if self.hits[mid] <= target:
                 self.low=mid+1
            else:
               high = mid-1
        
        return self.totalHits - self.low


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)