class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        lastKnownRight =-1
        s=list(dominoes)
        for index in range(len(dominoes)):
            if s[index]=="L":
                if lastKnownRight == -1:
                    # everything till index will be L -> ......L -> LLLLLLLL
                    j=index-1
                    while j>=0 and s[j]=="." :
                        s[j] ="L"
                        j-=1   
                else:
                    # there is right encountered, so need to balance out the R and L with . for odd length
                    # R....L -> RRRLLL and R...L -> RR.LL
                    left,right = lastKnownRight+1,index-1
                    while left<right:
                        s[left]="R"
                        s[right]="L"
                        left+=1
                        right-=1
                    lastKnownRight = -1
            elif s[index] =="R":
                if lastKnownRight!=-1:
                    for itx in range(lastKnownRight+1,index):
                        s[itx] ="R"
                lastKnownRight = index
        
        if lastKnownRight!=-1:
                for itx in range(lastKnownRight+1,len(dominoes)):
                        s[itx] ="R"
        return "".join(s)