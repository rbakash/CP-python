class Solution:
    def minOperations(self, n: int) -> int:
        # create the Arr
        arr=[]
        for i in range(n):
            arr.append((2*i)+1)
        number = 0
        if n&1:
            # if its odd
            number = arr[len(arr)//2]
        else:
            # if its even, then its avg of mid and mid-1
            # print(arr[n//2])
            number = (arr[n//2] + arr[(n//2)-1])//2
        
        numberOfOperations =0
        # print(arr,number)
        for index in range((n//2)):
            numberOfOperations += abs(number - arr[index])
        return numberOfOperations