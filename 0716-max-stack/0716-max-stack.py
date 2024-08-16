class MaxStack:

    def __init__(self):
        self.stack=[]
        self.heap=[]
        self.removed=set()
        self.count=0

    def push(self, x: int) -> None:
        heappush(self.heap,(-x,-self.count))
        self.stack.append((x,self.count))
        self.count+=1
    def findIndex(target):
        left,right = 0,len(self.sortedList)
        
        while left<=right:
            mid = (left + right)//2
            if self.sortedList[mid]<target:
                left = mid+1
            else:
                right = mid
        return left

    def pop(self) -> int:
        while self.stack and self.stack[-1][1] in self.removed:
            self.stack.pop()
        
        topElement,index = self.stack.pop()
        self.removed.add(index)
        return topElement

    def top(self) -> int:
        while self.stack and self.stack[-1][1] in self.removed:
            self.stack.pop()
        return self.stack[-1][0]

    def peekMax(self) -> int:
        while self.heap and -self.heap[0][1] in self.removed:
            heappop(self.heap)
        return -self.heap[0][0]

    def popMax(self) -> int:
        while self.heap and -self.heap[0][1] in self.removed:
            heappop(self.heap)
        topElement,index = heappop(self.heap)
        self.removed.add(-index)
        return -topElement


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()