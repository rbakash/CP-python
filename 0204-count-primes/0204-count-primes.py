class Solution:
    def countPrimes(self, n: int) -> int:
        if n <=2:
            return 0
        numbers=[True]*n
        numbers[0],numbers[1]=False,False
        for num in range(2,int(sqrt(n)+1)):
            if numbers[num]:
                numbers[num * num : n : num] = [False] * len(numbers[num * num : n : num])
                # for eachMultiple in range(num*num,n,num):
                #     numbers[eachMultiple]=False
        return sum(numbers)
                