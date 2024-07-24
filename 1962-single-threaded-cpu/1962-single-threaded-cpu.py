class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # sort the task based on Arrival time
        sortedTasks = [(avaiableAt,processingTime,index) for index,(avaiableAt,processingTime) in enumerate(tasks)]
        sortedTasks.sort()

        # minHeap to maintain the smallest processing job first
        minHeap=[]
        currentExecutionTime= sortedTasks[0][0]
        nextTaskIndex=0
        order=[]
        while len(order) < len(sortedTasks):

            while nextTaskIndex < len(sortedTasks) and sortedTasks[nextTaskIndex][0] <= currentExecutionTime:
                heappush(minHeap,(sortedTasks[nextTaskIndex][1],sortedTasks[nextTaskIndex][2]))
                nextTaskIndex+=1

            if minHeap:
                nextTask=heappop(minHeap)
                currentExecutionTime += nextTask[0]
                order.append(nextTask[1])
            else:
                currentExecutionTime = sortedTasks[nextTaskIndex][0]
        return order