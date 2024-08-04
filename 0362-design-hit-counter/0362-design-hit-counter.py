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
        low,high = self.low, self.totalHits-1
        
        while low<=high:
            mid = (low+high)//2
              
            if self.hits[mid] <= target:
                 low=mid+1
            else:
               high = mid-1
        self.low=low
        return self.totalHits - self.low


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)