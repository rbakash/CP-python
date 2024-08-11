class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        employeeKeyTime=defaultdict(list)
        for name,hourMinute in zip(keyName,keyTime):
            hour, minute = map(int, hourMinute.split(':'))
            time = hour * 60 + minute
            employeeKeyTime[name].append(time)
        result=[]
        for employeeName,time in employeeKeyTime.items():
            time.sort()
            queue=deque()
            for eachTime in time:
                queue.append(eachTime)
                if queue[-1] - queue[0]>60:
                    queue.popleft()
                if len(queue)>=3:
                    result.append(employeeName)
                    break
            
        return sorted(result)