from sortedcontainers import SortedList
class Solution:
    def maxTaskAssignEdi(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        print(SortedList(workers))
        heapify(workers)
        heapify(tasks)
        print(workers,tasks)
        maxTasks = 0
        while tasks and workers:
            currentStrength = heappop(workers)
            currentTask = tasks[0]
            
            if currentStrength >= currentTask:
                maxTasks+=1
                print(currentStrength,currentTask)
                heappop(tasks)
            elif pills>0 and currentStrength+strength>=currentTask:
                print(currentStrength,currentTask)
                maxTasks+=1
                pills-=1
                heappop(tasks)
        return maxTasks
    
    def maxTaskAssign(self,tasks, workers, pills, strength) ->int:
        
        workers.sort()
        tasks.sort()
        def checkIfKGuessedTasksCanBeCompleted(k)->bool:
            newTasks = SortedList(tasks[:k])
            # k strongest worker
            strongestWorkers = (workers[-k:])
            remainingPills = pills
            for eachWorker in strongestWorkers:

                if eachWorker >= newTasks[0]:
                    newTasks.pop(0)
                elif remainingPills and eachWorker + strength >= newTasks[0]:
                    # find the nearest task for new strength
                    index = newTasks.bisect_right(eachWorker + strength)
                    newTasks.pop(index-1)
                    remainingPills-=1
                else:
                    return False
            return True

        # Perform Binary search
        low,high = 0, min(len(workers),len(tasks))
        while low < high:
            mid = low + (high-low+ 1)//2
            if checkIfKGuessedTasksCanBeCompleted(mid):
                low = mid
            else:
                high = mid-1
        return low
