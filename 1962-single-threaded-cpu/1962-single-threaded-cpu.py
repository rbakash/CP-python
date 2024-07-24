class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # sort the task based on Arrival time
        earlierTasks = [(task[0],task[1],index) for index,task in enumerate(tasks)]
        earlierTasks.sort(key=lambda task: task[0])

        # minHeap to maintain the smallest processing job first
        minHeap=[]
        currentExecutionTime= earlierTasks[0][0]
        currentTaskEndTime=0
        nextEarliestTask=0
        order=[]
        isCpuIdle = True
        while len(order) < len(earlierTasks):

            while nextEarliestTask < len(earlierTasks) and earlierTasks[nextEarliestTask][0] <= currentExecutionTime:
                heappush(minHeap,(earlierTasks[nextEarliestTask][1],earlierTasks[nextEarliestTask][2]))
                nextEarliestTask+=1

            if minHeap:
                nextTask=heappop(minHeap)
                currentExecutionTime += nextTask[0]
                order.append(nextTask[1])
            else:
                currentExecutionTime = earlierTasks[nextEarliestTask][0]
        return order