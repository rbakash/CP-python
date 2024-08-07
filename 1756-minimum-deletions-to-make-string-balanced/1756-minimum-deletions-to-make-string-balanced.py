class Solution:
    def minimumDeletions(self, s: str) -> int:
        #Stack based 
        stack =[]
        minDeletion = 0
        for char in s:
            if stack and stack[-1] =='b' and char =='a':
                stack.pop()
                minDeletion +=1
            else:
                stack.append(char)
        return minDeletion

        # n = len(s)
        # aCount=[0]*n
        # bCount = [0]*n
        # runningCount =0
        # minDeletion = n
        # for index in range(n):
        #     bCount[index] = runningCount
        #     if s[index]=='b':
        #         runningCount+=1
        # runningCount = 0
        # for index in range(n-1,-1,-1):
        #     aCount[index]=runningCount
        #     if s[index]=='a':
        #         runningCount+=1
        
        # for i in range(n):
        #     minDeletion = min(minDeletion, aCount[i]+bCount[i])
        # return minDeletion