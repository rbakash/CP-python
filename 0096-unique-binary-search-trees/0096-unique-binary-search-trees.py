class Solution:
    def numTrees(self, n: int) -> int:
        sequence= list(range(1,n+1))
        maxBST=[0]*(n+1)
        maxBST[0],maxBST[1]=1,1
        
        for ithNode in range(2,n+1):
            # for each ith node we can have multiple bst with root
            # eX : 1,2,3,4 then if ithNode is 3 , 
            # then bst can have 1 and 2 as root, hence we need to compute for each of the root
            for jthRoot in range(1,ithNode+1):
                maxBST[ithNode]+=maxBST[jthRoot-1]*maxBST[ithNode-jthRoot]
        
        return maxBST[n]