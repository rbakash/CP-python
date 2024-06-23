class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letterLog, digitLog =[],[]
        for eachLog in logs:
            identifier,log = eachLog.split(" ",1)
            if (log[0]).isalpha():
                letterLog.append((identifier,log,eachLog))
            else:
                digitLog.append((identifier, log,eachLog))
        letterLog.sort(key = lambda x: (x[1],x[0]))
        letterLog+=(digitLog)
        letterLog = [log[2] for log in letterLog]
        print(letterLog)
        return letterLog