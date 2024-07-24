class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # sort the task based on Arrival time
        sortedTasks = [(task[0],task[1],index) for index,task in enumerate(tasks)]
        sortedTasks.sort(key=lambda task: task[0])

        # minHeap to maintain the smallest processing job first
        minHeap=[]
        currentExecutionTime= sortedTasks[0][0]
        nextAvaliableTask=0
        order=[]
        while len(order) < len(sortedTasks):

            while nextAvaliableTask < len(sortedTasks) and sortedTasks[nextAvaliableTask][0] <= currentExecutionTime:
                heappush(minHeap,(sortedTasks[nextAvaliableTask][1],sortedTasks[nextAvaliableTask][2]))
                nextAvaliableTask+=1

            if minHeap:
                nextTask=heappop(minHeap)
                currentExecutionTime += nextTask[0]
                order.append(nextTask[1])
            else:
                currentExecutionTime = sortedTasks[nextAvaliableTask][0]
        return order