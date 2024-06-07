class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        if k==1:
            return 1
        k-=1
        for number in range(2,n+1):
            if n % number ==0:
                k-=1
            if k==0:
                return number

        return -1  
        