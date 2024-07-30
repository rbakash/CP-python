class MedianFinder:

    def __init__(self):
        self.nums=[]
        self.length=0

    def addNum(self, num: int) -> None:
        self.length+=1
        if not self.length :
            self.nums.append(nums)
        else:
            index = bisect.bisect_left(self.nums, num)
            self.nums.insert(index,num)


    def findMedian(self) -> float:
        self.nums.sort()

        if self.length & 1:
            return self.nums[self.length//2]
        else:
            return 0.5* (self.nums[self.length//2] + self.nums[self.length//2-1])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()