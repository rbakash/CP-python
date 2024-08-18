class Solution:
    def myPow(self, x: float, n: int) -> float:
        def binaryExp(x,n):
            if n==0:
                return 1
            if n<0:
                return 1/binaryExp(x,-n)
            if n & 1:
                return x*binaryExp(x*x,(n//2))
            else:
                return binaryExp(x*x,(n//2))
        return binaryExp(x,n)